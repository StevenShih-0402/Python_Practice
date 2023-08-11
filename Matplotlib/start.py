import matplotlib.pyplot as plt

''' pyplot: 繪製折線圖的模組，用plot([x座標], [y座標])建立資料點，show()顯示圖表'''
plt.plot([1,3,5], [2,7,5])
plt.show()

# 兩組資料點：相同的X軸上有兩條折線
plt.plot([2,4,7,9], [[8,5], [5,9], [7,7], [10,9]])
plt.show()

''' 圖例: 透過rc()設定執行環境'''
# 設定中文字形
plt.rc("font", family="Klee One")

# 透過label方法設定圖例，legend方法顯示圖例, xlabel、ylabel設定軸線標題
plt.plot(
    [2,4,7,9], 
    [[8,5], [5,9], [7,7], [10,9]],
    label=["組別A", "組別B"]
)
plt.legend()
plt.xlabel("得分")
plt.ylabel("失分")
plt.show()

# 匯入CSV檔
import csv
file=open("testcsv.csv", encoding="utf-8")
reader=csv.reader(file)
header=next(reader)

x=[]
y=[]
for row in reader:
    x.append(int(row[0]))
    y.append([int(row[1]), int(row[2])])

plt.plot(
    x,
    y,
    label=header[1:3]
)
plt.legend()
plt.xlabel(header[0])
plt.ylabel("人數")
plt.show()