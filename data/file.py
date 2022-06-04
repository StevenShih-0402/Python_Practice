#檔案物件 = open(檔案路徑, mode = 開啟方式, encoding = 編碼)         讀取:r 寫入:w 讀寫:r+
#讀取：檔案物件.read()
#寫入：檔案物件.write("內容")
#關閉：檔案物件.close()

#for 變數 in 檔案物件:      將檔案物件一行一行讀出

file = open("wahaha.txt", mode = "w", encoding = "utf-8")   #開啟(建立)
file.write("xi le hello?\n是在哈囉？")                       #操作
file.close()                                                #關閉(檔案資源釋放)

#以上三個流程實務通常會用：
with open("dio.txt", mode = "w", encoding = "utf-8") as eliF:
    eliF.write("wryyyyyyyy\nyyyyyyyyyrw")

#with會自動執行close

with open("wahaha.txt", mode = "r", encoding = "utf-8") as file:
    data = file.read()
print(data)

#-----------------------------------------------------------------------------------------------------------------------------
#案例：寫入數字並將內容相加
sum = 0

with open("cul.txt", mode = "r+", encoding = "utf-8") as cu:
    cu.write("11\n22\n33\n44\n55")
    for num in cu:
        sum += int(num)

print(sum)
#JSON資料：(import json)
# 讀取到的資料 = json.load(檔案物件)
# json.dump(要寫入的資料, 檔案物件)

import json
with open("confit.json", mode = "r", encoding = "utf-8") as word:
    result = json.load(word)

print(result)                               #以python字典的形式進行
print("name: ", result["name"])                 
print("version: ", result["version"])

#修改變數的資料後，再將最新的資料複寫回檔案
result["name"] = "Steven"
with open("confit.json", mode = "w", encoding = "utf-8") as word:
    json.dump(result, word)




