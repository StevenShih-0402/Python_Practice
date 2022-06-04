# Q印出元素
sequence = ['a', 'b', 'c', 'd', 'e']
for letter in sequence:
    print(letter)

# Q印出編號與元素-使用 enumerate
# for 索引位置,變數 in enumerate(陣列)
namelist = ['adm', 'bob', 'cat', 'david', 'elephant', 'fox']
for number ,item in enumerate(namelist):
    if(number % 2 == 1):
      print("位置編號:",number)
      print("元素內容:",item)
    #印出串列中INDEX位置
       #印出對應位置的名字

# Q:range 範例
sum =0
count =1
# for i in range(10): 累加10次
#    #  sum =sum +count  累加1 

# print(sum) 

# sum =0
# for i in range(1, 101): #調整range為到100的值，記得關門數字要+1
#     sum =sum + i     
# print(sum)    # 使用sum 和i 做相加，並累積到sum
   #迴圈結束後，印出sum

#Q:range 範例用跳間隔
for i in range(0, 10, 2):
    print(i)

#小試身手: for 應用 印出單字
# Words = "abcdefghijklmnopqrstuvwxyz"
# for i in Words:
#    print(i)
 
# # Q: Break練習
# ANIMALS = ['鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗', '豬']
# for animal in ANIMALS:
#     if animal == "蛇":
#         break
#     else:
#         print(animal)

# Q: continue 練習，結合for印出偶數 ，可結合 mod(求餘數功能)
# 如果數字大於6則停止迴圈
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# for i in numbers:
#    if(i > 6):
#       continue
#    if(i % 2 == 0):
#       print(i)
 
# for i in range(4):
#    if(i < 3):
#       pass
#    print(i, i+1)

# Q: for 應用  印出直角三角形
'''tip: 
1.讓使用者輸入三角形層數
2.建立一個FOR
3.根據現在的層數印出對應的星星數量 (參考string的: S*N 重複字串方法)
'''
# tall = eval(input("輸入層數: "))
# for i in range(tall):
#    print("*"*(i+1))

# 九九乘法表
limit = eval(input("你要多少?"))
for i in range(1,limit+1):
   for j in range(1,10):
      print("{i} x {j} = {ans}".format(i = i, j = j, ans = i*j))
   print()

# test =["happy","birthday","to","You"]

# for letter in test :
#     if letter =="happy":
#         continue
#         print(1)    
#     elif letter == "to":  
#         print(letter)  
#         break
#     else :
#         print(letter)