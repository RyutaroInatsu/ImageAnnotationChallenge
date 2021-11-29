import csv
import os
import random
import re
import time

import bs4
import requests
from requests_html import HTMLSession

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
}

label_path = "./inputs/albanycountryfasteners/label.csv"

url = "https://www.albanycountyfasteners.com/Category/Screws_And_Bolts"
# https://www.albanycountyfasteners.com/Category/Screws_And_Bolts?CatListingOffset=288&Offset=288&Per_Page=144&Sort_By=bestsellers
# url = "https://www.albanycountyfasteners.com/Category/Washers"
# url = "https://www.albanycountyfasteners.com/Category/Nuts"

fastener_attr_list = {
    "Color": "",
    "Drive Style": " drive",
    "Head Style": " head",
    "Point Type": " point",
    "Thread Type": " thread",
}

session = HTMLSession()
image_counter = 0
item_counter = 0

for i in range(0, 10):
    print(f"Now page: {i+1}")
    now_url = url
    if i > 0:
        now_url += (
            f"?CatListingOffset={i*144}&Offset={i*144}&Per_Page=144&Sort_By=bestsellers"
        )

    item_list_page = session.get(now_url, headers=headers)
    item_list_page.html.render(timeout=20)

    soup = bs4.BeautifulSoup(item_list_page.content, "html.parser")

    item_url_list = soup.find_all("a", {"class": "level-2"})
    for item_url in item_url_list:
        # for item_url in item_url_list:
        print(f"Item count: {item_counter+1}")
        item_page = session.get(item_url["href"], headers=headers)
        item_page.html.render(timeout=30)

        # re
        # -[0-9]-resize
        # print(item_list_page.text)
        soup2 = bs4.BeautifulSoup(item_page.content, features="lxml")
        img = soup2.find("input", {"name": "prodImage"})

        # image url pattern
        # https://www.albanycountyfasteners.com/-8-stainless-steel-square-drive-bugle-head-deck-screws/6010000.htm
        # https://www.albanycountyfasteners.com/mm5/graphics/00000001/square-drive-bugle-head-305-stainless-steel- 1 -resize-min _300x300 .jpg item thumbnail
        # https://www.albanycountyfasteners.com/mm5/graphics/00000001/square-drive-bugle-head-305-stainless-steel- 1 -resize-min.jpg
        # https://www.albanycountyfasteners.com/mm5/graphics/00000001/square-drive-bugle-head-305-stainless-steel- 2 -resize-min.jpg
        # https://www.albanycountyfasteners.com/mm5/graphics/00000001/Star-Drive-Stainless-Steel-Bugle-Head-Deck-Screws- 2(RESIZE)-min.jpg
        # https://www.albanycountyfasteners.com/mm5/graphics/00000001/Phillips-Pan-Head-Machine-Screws-18-8SS-Product- 1 -(RESIZE)-min_300x300.jpg
        # https://www.albanycountyfasteners.com/mm5/graphics/00000001/8204-004-2.jpg
        splitted_url = re.split(r"-[0-9]-?(\(RESIZE\)|-resize)", img["value"])

        # get tags
        tag_list = ["nut", "filename"]
        for attr in fastener_attr_list:
            div_element = soup2.find("div", text=attr)
            if div_element is None:
                continue

            next_element = div_element.findNext("div")
            if next_element is None:
                continue

            if next_element.text is None:
                continue

            tag_list.append(
                next_element.text.rstrip() + fastener_attr_list[attr]
            )  # to remove whitespaces and newlines

        # get images
        for num in range(1, 4):
            if len(splitted_url) > 1:
                image_url = (
                    splitted_url[0] + "-" + str(num) + splitted_url[1] + "-min.jpg"
                )
            else:
                image_url = splitted_url[0]

            response = requests.get(image_url, headers=headers)
            if response.status_code != 200:
                image_url = (
                    splitted_url[0] + "-" + str(num) + "-" + splitted_url[1] + "-min.jpg"
                )
                response = requests.get(image_url, headers=headers)
                if response.status_code != 200:
                    continue

            filename = f"{str(image_counter).zfill(6)}.jpg"
            tag_list[1] = filename

            with open(os.path.join("./inputs/albanycountyfasteners/screw/", filename), "wb") as file:
                file.write(response.content)
                image_counter += 1

            with open(label_path, "a", newline="") as label_file:
                wr = csv.writer(label_file, quoting=csv.QUOTE_ALL)
                wr.writerow(tag_list)

        time.sleep(random.randint(5, 10))
        item_counter += 1


# if soup2.find("th", text="Mounting Hole") != None:
#     print(soup2.find("th", text="Mounting Hole").findNext("td").text)


# wire_attr_list = [
#     "Application",
#     "Standard (CN1/CN2)",
#     "Connector type CN1",
#     "Connector type CN2",
#     "Type",
#     "Color",
#     "Cable type",
#     "Processing method",
#     "SPecifications",
#     "Wire Connection",
#     "CN1 connector direction",
#     "CN2 connector direction",
#     "CN1",
#     "CN2",
#     "Connector 1",
#     "Connector 2",
#     "Connector shape",
#     "Terminal shape"
# ]
