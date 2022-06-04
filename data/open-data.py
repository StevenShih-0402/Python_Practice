#網路連線
# import urllib.request as re

# src = "https://www.tku.edu.tw/"

# with re.urlopen(src) as response:
#     data = response.read().decode("utf-8")           #將模組re裡面的urlopen方法打開src以後放入response，再用read讀出原始碼(HTML,CSS,JS)，並用decode解碼顯示中文

# print(data)

#串接、擷取公開資料

import urllib.request as re
import json

src = "	https://data.taipei/api/v1/dataset/13f0e277-8eaa-4ca1-ab9f-dcb99d9c9a77?scope=resourceAquire"       #臺北市南港軟體工業園區廠商資料名錄

with re.urlopen(src) as response:
    data = json.load(response)      #裡面的資料為json格式，在python是以字典方式呈現

# print(data)

#擷取特定資料

clist = data["result"]["results"]           #我們只要 "所有資料"(data) 底下的 "result" 的 "公司名錄"(results)

with open("名稱與統編.txt", "w", encoding = "utf-8") as file:
    for run in clist:
        file.write(run["﻿統編"] + "/" + run["公司名稱"] + " -- " + str(run["_id"]) + "\n")