import requests
import json

url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
res = requests.get(url)
print(f"Status code: {res.status_code}")

response_dict = res.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)

