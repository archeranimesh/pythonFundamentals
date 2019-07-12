import requests

URL = "http://shibe.online/api/shibes?count=1"

response = requests.get(URL)

print("Response status code: ", response.status_code)

if response.status_code == 200:
    response_json = response.json()
    print("response json: ", response_json)
