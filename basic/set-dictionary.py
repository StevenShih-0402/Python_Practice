#集合
s1 = {3,4,5}
print(10 in s1)
print(10 not in s1)     #確認資料有沒有在裡面

s2 = {5,6,7,8}
print(s1&s2)            #交集：兩個集合相同的部分
print(s1|s2)            #聯集：兩個集合的所有資料(重複的只顯示一次)
print(s1-s2)            #差集：s1減去和s2重複的資料
print(s1^s2)            #反交集：兩個集合不重複的部分

w = set("hello")        #將字串變成集合
print("h" in w)
print("s" in w)

#字典(key-value)
book = {"apple":"蘋果", "wow":"哇"}
book["apple"] = "小蘋果"                #替換字典內容
print(book["apple"])

print("apple" in book)                  #尋找key有沒有在字典裡
print("janifor" in book)

del book["apple"]
print(book)

dic = {x:x*2 for x in [3,4,5]}          #以列表([])的資料為基礎產生字典
print(dic)