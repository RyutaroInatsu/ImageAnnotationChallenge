import requests

resp = requests.post("http://localhost:5000/api",
                     files={"file": open('./inputs/test/20191123_141750.jpg', 'rb')})

print(resp.status_code)
print(resp.json())
