import datetime
# list 計算LIST長度練習 ，使用len
fruits = ["apple", "banana", "cherry"]
水果數量= len(fruits)
print(水果數量)

# list 取值練習
fruits = ["apple", "banana", "cherry"]
print(fruits[2])
print(fruits[-2])
print(fruits[0:2])
print(fruits[-3:])
print(fruits[0:2])

# list取值練習2
seasons = ["spring", "summer", "fall", "winter"]

print(len(seasons))
print(seasons[2])
print(seasons[1:4:2])

# seasons[3] = "Winter"
# print(seasons[:])

# append練習 -guava
fruits.append("guava")
# print("after:",fruits)

# Insert練習 將coconut加入第三個位置
fruits.insert(3,"coconut")
# print("after insert:",fruits)

# extend 練習
fruit_1 = ["apple", "avocado", "banana"]
fruit_2 = ["cherry", "coconut", "guava"]
fruit_1.extend(fruit_2)
print(fruit_1)
 
# 綜合練習
half_zodiac1 = ["Rat", "Ox", "Tiger", "Dragon", "Snake"]
half_zodiac2 = ["Horse", "Goat", "Monkey", "Rooster", "Dog"]

'''
請新增Rabbit到Tiger與Dragon之間
half_zodiac2最後新增一個Pig
將half_zodiac2每個元素獨立合併到half_zodiac1
'''
 

# # remove練習
fruits.remove("cherry")
# #pop練習
fruits.pop()
print(fruits)


# slicing 在尾巴加入元素
fruits[len(fruits):] = ["guava","lichee"]
print(fruits)
# slicing 在串列起始加入元素
fruits[:0] = ["strawberry"]
print(fruits)

# 分割範例
strs = "Line1 Line2 Line4"
print(strs.split())  #  預設以空格为分隔符號


## 建立一Stock_number串列儲存分割的字串
Stock_full = "1101.tw"
stok = Stock_full.split(".")
print(stok)



## 字串判斷-起始判斷
keyword = ("美麗華", "三貂角", "台北101")
LandMark = "台北101是台灣最美的景點"
key = LandMark.startswith(keyword)
print(key)
 
# Q :請用十行以內的程式將下面七言絕句印出加上今日日期，輸出範例如下:
''' 
勸君莫惜金縷衣
勸君惜取少年時
花開堪折直須折
莫待無花空折枝
2020-03-06
'''
# 提示  分割句子可以用.split("要分割的符號") ；
#       轉日期為文字格式使用.strftime("要轉換的格式")   %Y 為四位數年分，%m 為月份， %d 為日期
sentence = "勸君莫惜金縷衣,勸君惜取少年時,花開堪折直須折,莫待無花空折枝"
 

## 其他應用 max,min,sum,sorted
tsmc = [599.573,571,575,575,580,571,572,574,602,588,600]

ans = []
ans.append(max(tsmc))
ans.append(min(tsmc))
ans.append(sum(tsmc))
tsmc = sorted(tsmc)

print(ans)
print(tsmc)
# 解包後指定
myAddress=["台北市","中正區","中正路100號"]
'''
請在一行內設置三個變數city,dict,road 分別指定myAddress的元素
'''
