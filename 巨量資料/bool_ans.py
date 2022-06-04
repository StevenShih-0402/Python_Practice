# 文字也可以用ASCII碼的大小做比較
a = "A" > "B"
print(a)
#Q: 結合邏輯運算符
'''台灣大藥局有兒童口罩212個，成人口罩已完售
   設定條件一:兒童口罩>0個
   設定條件二:成人口罩 >0個
'''
conditon1 = True
conditon2 = False
print(conditon1 or conditon2) #任一條件成立
print(conditon1 and conditon2) #兩者條件皆成立
print(not conditon1) #反轉條件一
'''
西元年份除以4可整除，且除以100不可整除，為閏年。
西元年份除以400可整除，為閏年。
'''
# Q 閏年的判斷
import datetime
year = 2100
if((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)) :  #閏年條件
    print("閏年")
else:
    print("Not")


# Q :IF else練習，請讓使用者輸入兩個數字(被除數與除數)，若除數不為零，顯示相除後的結果，
#   若除數為零，則顯示”不能相除”
no_1 = eval(input("被除數:"))  #使用者輸入被除數
no_2 =  eval(input("除數:")) #使用者輸入除數

if(no_2 != 0) :   #判斷條件成立
   rlt=no_1/no_2
   print(rlt)                #印出結果
else:            #不成立
   print("不能相除")                #顯示不能相除

# Q: 多重條件分支~
# 請讓使用者輸入交易競賽名次
# 若交易比賽成績獲得第一名，印出獎金1萬元；
# 得到第二名印出獎金5000元；
# 獲得第三名則印出獎金3000元；
# 其他名次印出獲得獎狀一張

no = int(input("請輸入名次"))
#判斷no的值，並印出獎勵
if(no == 1):
   print("獎金1萬元")
elif(no == 2):
   print("獎金5000元")
elif(no == 3):
   print("獎金3000元")
else:
   print("獎狀一張")

print("冠軍")if(no == 1)else print("不是冠軍")        #單行判斷式(類似JAVA的?:)

# Q: is None 的應用 : 請用IF ELSE 判斷aDate是否為空值(NONE)，
# 如為空值，aDate請帶入今日的日期可使用datetime.date.today()；若非空值直接印出
#
aDate = None  #None沒有設定，以空值稱呼
print(datetime.date.today())if(aDate is None)else print(aDate)
    

    
