#載入sys模組

import sys as S                         #也可以將S的部分直接用sys呼叫

print(S.platform)                       #顯示作業系統
print(S.maxsize)                        #顯示整數最大值

#建立geometry模組，載入使用

#import geometry

# result = geometry.distance(1,1,5,5)
# print(result)

# print(geometry.slope(1,1,5,5))

#搜尋模組路徑

S.path.append("modules")                #在模組的搜尋路徑中『新增路徑』，因為原先的搜尋路徑不包含我們新建的資料夾，不新增的話系統會找不到
print(S.path)                           #顯示模組的搜尋路徑

import geometry
print(geometry.distance(10,10,50,50))