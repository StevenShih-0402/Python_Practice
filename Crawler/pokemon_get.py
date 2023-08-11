import requests as res
from bs4 import BeautifulSoup

respons = res.get("http://jimmypm.ehosting.com.tw/new001151.htm")
respons.encoding = "utf-8"

soup = BeautifulSoup(respons.text, "html.parser")
print(soup.prettify())