#判斷式

x = input("enter a number: ")       #使用者輸入
x = int(x)                          #將字串轉成int才能用判斷式

if(x > 200):
    print("true")
elif(x >100):
    print("aaaaa")
else:
    print("false")

y1 = int(input("請輸入數字壹："))
y2 = int(input("請輸入數字貳："))

op = str(input("輸入+,-,*,/"))

if(op == "+"):
    print(y1+y2)
elif(op == "-"):
    print(y1-y2)
elif(op == "*"):
    print(y1*y2)
elif(op == "/"):
    print(y1/y2)
else:
    print("WTF")