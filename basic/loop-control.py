#break:強制結束迴圈
x = 0
sum = 0
while(x <= 5):
    sum += 2
    if(sum >= 3):
        break
    print(sum)

#continue:強制進入下一輪迴圈
jump = 2
for i in[1,2,3,4,5]:
    if(i == jump):
        continue
    print(i)

#else:在迴圈結束前，再執行這個區塊一次
total = 0
for n in range(11):
    total += n
else:
    print(total)

#練習→求平方根
n = input("輸入整數：")
n = int(n)

for o in range(n):
    if(o * o == n):
        print("整數平方根：", o)
        break   #透過break跳出的迴圈，不會執行else
else:
    print("沒有平方根")
