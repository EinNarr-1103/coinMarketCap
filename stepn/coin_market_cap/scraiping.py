
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#URLの指定
url = 'https://coinmarketcap.com/'

#ユーザージェントの設定
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text.encode(r.encoding), "html.parser")
print(soup)

# #trをすべて取得
for tr in soup.find_all('tr'):
    coinCon = tr.find("a")
    if coinCon != None:
        coinName = coinCon.text
        price = tr.find("a", { "class" : "price" })
        rate = tr.find("td", {"class" : "percent-24h"})

        print("■" + coinName)
        print("price：" + price.text)
        print("rate24h:" + rate.text)