import pandas as PD

# # 建立Series(單維度資料):列，陣列
# data = PD.Series([15, 20, 5])       #int64: 資料型態為"64位元的int"
# # print(data)

# # 基本Series操作
# print(data.max())
# print(data.median())
# data = data * 2
# print(data)

# data = data == 30
# print(data)

# 建立DataFrame(多維度資料):表格，字典
box = PD.DataFrame({
    "name":["Steven", "Jack", "Tom"],
    "salary":[30000, 10000, 40000]
})
print(box)
print("\n")
print(box["name"])
print("-------------------------")
print(box.iloc[1])      #印出第二列