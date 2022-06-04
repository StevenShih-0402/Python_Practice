from os import sep
import pandas as PD

# 建立Series與其索引
data = PD.Series([4, -8, 7, 6, 3], index=["星", "爆", "氣", "流", "斬"])
# print(data)

# 觀察資料
# print("資料型態", data.dtype)
# print("資料數量", data.size)
# print("資料索引", data.index)

# 尋找資料
# print(data[2], data[4])
# print(data["氣"], data["斬"])

# 基本運算(統計、順序)
# print("最大值", data.max())
# print("總和", data.sum())
# print("標準差", data.std())
# print("中位數", data.median())
# print("最大的三個數", data.nlargest(3))
# print("最小的兩個數", data.nsmallest(2))

# 字串運算(串接、搜尋、取代)
chinese = PD.Series(["你好", "XieXie", "小籠包", "再見"])

print(chinese.str.lower(),"\n", "--------------")                      #全部變小寫
print(chinese.str.upper(),"\n", "--------------")                      #全部變大寫
print(chinese.str.len(),"\n", "--------------")                        #每個字串的長度
print(chinese.str.cat(sep=" (～￣▽￣)～ "),"\n", "--------------")     #用sep將字串連接
print(chinese.str.replace("你好", "NiHao"),"\n", "--------------")     #將前面的字串『暫時』替換成後面的字串
print(chinese.str.contains("i"))                                       #判斷每個字串內有沒有i存在