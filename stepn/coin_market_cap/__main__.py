import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://pro-api.coinmarketcap.com"
END_POINT = "/v1/cryptocurrency/listings/latest"

headers = {
  "X-CMC_PRO_API_KEY": os.environ["ACCESS_KEY"],
  "Accept": "application/json"
}
res = requests.get(BASE_URL + END_POINT, headers=headers)
if (res.ok):
  json = json.loads(res.text)
  print(json)
else:
  print("api call failed!")