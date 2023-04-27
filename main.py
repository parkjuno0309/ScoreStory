import requests
from pprint import PrettyPrinter
import json

BASE_URL = "https://api.sportsdata.io"
API_KEY = "5dfb1139e28a480d9e3f84f84f340c2b"
printer = PrettyPrinter()

date = input("Enter date of MLB game: ") # format should be "2017-JUL-31"

# we should clean the data above using chatGPT?

request_url = f"{BASE_URL}/v3/mlb/stats/json/BoxScores/{date}?key={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200: # 200 means successful
    data = response.json()

printer.pprint(data[0])

# data_dict = json.loads(data)
# keys = data_dict.keys()
# print(keys)
