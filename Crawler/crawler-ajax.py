#抓取目標原始碼(ajax的網頁，要連接到真正連線的網址)
#F12 → XHR → 找到對應的文件 → 複製header的URL
import urllib.request as req

url = "https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=c02796041202de367c84b7343c7c9b1c"
#建立一個request物件，附加request header的資訊(模擬正常使用者的狀態)
uusseerr = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
})

with req.urlopen(uusseerr) as response:
    data = response.read().decode("utf-8")

#解析原始碼，取得特定的內容(kkday的資料屬於JSON格式)
import json

data = json.loads(data)     #把原始的JSON解析成Python的字典
posts = data["data"]["homepage_product_group"][1]["prod_list"]       #從最外層一層一層往內找，直到想找的資料所在的那層為止
for key in posts:
    print(key["name"])
