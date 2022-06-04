#抓取目標原始碼
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"

#建立一個request物件，附加request header的資訊(模擬正常使用者的狀態)
uusseerr = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
})

with req.urlopen(uusseerr) as data:
    post = data.read().decode("utf-8")

#解析原始碼，取得特定的內容
import bs4
root = bs4.BeautifulSoup(post, "html.parser")   #beautifulSoup套件：協助解析HTML文件
posts = root.find_all("div", class_ = "title")

for catch in posts:
    if(catch.a != None):
        print(catch.a.string)