from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

import os, requests, misumi_directories, misumi_url_list

class MisumiScraping():
    """
    Class of scraping from misumi.
    """

    def __init__(self):
        # settings
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

        # make headless browser
        self.browser_options = ChromeOptions()
        self.browser_options.add_argument('--user-agent='+self.user_agent)
        self.browser_options.add_argument('--disable-extensions')
        self.browser_options.set_headless()

        # for requests library
        self.headers = {
            'User-Agent': self.user_agent,
            "Upgrade-Insecure-Requests": "1",
            "DNT": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate"
        }

    def execute_scraping(self, target_urls : list, directory_path : str, scraping_limit :int = 10000):
        """
        Execute scraping from target url

        Parameters
        -----------------
        target_url : list
            target page list of misumi page.(ex: https://jp.misumi-ec.com/vona2/mech_screw/M3303000000/M3303010000/)

        directory_path : str
            saving directory of images
        """

        try:
            driver = webdriver.Chrome(ChromeDriverManager().install(), options= self.browser_options)
            driver.set_window_size(800, 600)

            page_count = 1
            saved_image_count = 1

            for target_url in target_urls:
                while True:
                    if saved_image_count > scraping_limit:
                        print(f"Scraping limit({scraping_limit} has reached.")
                        break

                    print(target_url + f"?Page={page_count}")
                    driver.get(target_url + f"?Page={page_count}")

                    # collect source urls of all images.
                    imgs = driver.find_elements_by_xpath("//p[@class='mc-img']/img")
                    print(len(imgs))

                    if len(imgs) == 0:
                        print(f"There is no more page. Page count was {page_count}")
                        break

                    for img in imgs:
                        image_url:str = img.get_attribute("src")
                        print(image_url)

                        # TODO
                        # high-res: https://content.misumi-ec.com/image/upload/t_product_main/v1/p/jp/product/series/110300259460/110300259460_001.jpg?$product_main$
                        # low-res: https://content.misumi-ec.com/image/upload/t_product_view_b/v1/p/jp/product/series/110300259460/110300259460_001.jpg?$product_view_b$

                        # save images
                        response = requests.get(image_url, headers=self.headers)
                        if response.status_code == 200:
                            with open(os.path.join(directory_path, f"{str(saved_image_count).zfill(6)}.jpg"), "wb") as file:
                                file.write(response.content)
                                saved_image_count += 1

                    page_count += 1

        except Exception as err:
            print(err)
        finally:
            driver.quit()

if __name__ == '__main__':
    misumi_dirs = misumi_directories.MisumiDirectories("../inputs/misumi_dataset")
    misumi_dirs()
    misumi_scraping = MisumiScraping()

    # for dirpath, url_list in misumi_url_list.misumi_dir_url_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.cable_accessories_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.cable_bushing_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.cable_gland_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.cable_organization_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.computer_av_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.cordsets_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.crimp_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.electrical_conduits_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.electrical_tubing_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.electrical_wiring_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.equipment_specific_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.inserts_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.lan_industrial_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.nuts_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.screws_bolts_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.shims_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.soldering_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.specialized_wiring_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.washers_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.wire_cable_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.wire_ducts_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))

    # for dirpath, url_list in misumi_url_list.wiring_connectors_dict.items():
    #     misumi_scraping.execute_scraping(url_list, os.path.join(misumi_dirs.misumi_dataset_rootpath, dirpath))
