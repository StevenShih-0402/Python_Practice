#有序可變列表list
li = [1,2,3,4,5]
print(li)
li[1:3] = []            #刪除範圍內的東西
print(li[1:4])
li = li + [5,6]
print(li)
print(len(li))
star = [[7,8,7],[6,3]]
print(star[1][1])
star[0][0:2] = [5,5,5]
print(star)

#有序不可變列表tuple
data = (1,2,3,4)
print(data)
data[1] = 6         #error
