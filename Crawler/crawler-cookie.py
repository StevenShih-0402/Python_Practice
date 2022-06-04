#抓取目標原始碼
import urllib.request as req

def getData(url):
    #建立一個request物件，附加request header的資訊(模擬正常使用者的狀態)
    uusseerr = req.Request(url, headers = {
        "cookie":"over18=1",    #為了通過年齡認證
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    })

    with req.urlopen(uusseerr) as data:
        post = data.read().decode("utf-8")

    #解析原始碼，取得特定的內容
    import bs4
    root = bs4.BeautifulSoup(post, "html.parser")
    posts = root.find_all("div", class_ = "title")

    for catch in posts:
        if(catch.a != None):
            print(catch.a.string)

    #抓取上一頁的連結
    nextlink = root.find("a", string="‹ 上頁")      #找到內文是 "< 上頁" 的a標籤
    return nextlink["href"]


#主程序: 抓取多個頁面的標題
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0       #要擷取的頁面數量
while count < 5:
    url = "https://www.ptt.cc" + getData(url)       #/bbs/Gossiping/index.html 是getData會擷取到的href內容，與標頭結合後就能成為上一頁的網址
    count += 1
