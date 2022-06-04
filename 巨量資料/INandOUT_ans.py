##文字輸入1
# myName = input("")
# print(myName)

# ##文字輸入2
# myName = input("請輸入你的大名:")
# print(myName)


#數字輸入
# Num1 =eval(input("請輸入你的幸運數字:"))
# print("你的幸運號碼是:%.f" %Num1)


num_1 = 2020
num_2 = 123.456
txt = "LoveTaiwan"
# ##整數顯示
#print("|%d|" %(num_1))
# print("|%5d|" %(num_1))

##浮點數顯示
# print("|%3.2f|" %(num_2))
# print("|%8.1f|" %(num_2)) 

# ##文字顯示
# print("|%s|" %(txt)) 
# print("|%15s|" %(txt))

##調整對齊方式為靠左對齊

##format輸出
# print("{:4d}".format(num_1))
# print("{:3.2f}".format(num_2))
# print("{:s}".format(txt)) 

## format 輸出2
year = 2020
month = 9
date =24
print("today is {y} {m:2d} {d}".format(d=date,m=month,y=year))
# 月 日 年
print("today is {} {} {}".format(month,date,year))