#隨機模組(random)
import random

data1 = random.choice([4,8,7,6,3])          #隨機選取一個數字
print(data1)

data2 = random.sample([1,68,14,7,25], 2)    #隨機選取指定數量的數字
print(data2)

data3 = [1,7,13,19,29]
random.shuffle(data3)                       #隨機調換順序(洗牌)
print(data3)

data4 = random.random()                     #隨機取得0~1之間的亂數(random模組中的random函式)，每個數機率相同
print(data4)

data5 = random.uniform(63, 87)              #隨機取得63~87之間的亂數，每個數機率相同
print(data5)

data6 = random.normalvariate(100, 10)       #常態分配亂數(平均數，標準差)，會盡量產生在(n-σ)與(n+σ)範圍內的亂數
print(data6)

#統計模組

import statistics as sta

data7 = sta.mean([30,40,50])                #平均數
print(data7)

data8 = sta.median([2,3,5,7,11,97])         #中位數
print(data8)

data9 = sta.stdev([30,40,50])               #標準差
print(data9)
