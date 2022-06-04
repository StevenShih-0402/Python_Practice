
##整數
print(int())
print(int(3.6))
print(int("10"))

##浮點數
print(float())
print(float(113))
print(float(-15.6))
print(float("9527"))

##運算子
x = 4
y = 7
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)
print(+x)
print(-x)

##其他應用
#求餘數，運算結果請用answer紀錄並印出
# divmod(x, y)
x=63
y=6
answser = divmod(x, y)
print(answser)
##多次方項，運算結果請用answer紀錄並印出
# pow(x, y)
x=2
y=5
print(pow(x, y))

##取小數點N位，運算結果請用answer紀錄並印出
# round(x[, n])
x=3.1415926
n=3
answer = round(x)
print(answer)
answer = round(x,n)
print(answer)
##換算為二進位的數字，運算結果請用answer紀錄並印出
#bin(b)
b=6
answer = bin(b)
print(answer)
