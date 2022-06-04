import random

bomb = random.randint(1,100)  #隨機產生1-100之間的亂數
print("金庫密碼已設置")
guess = 0
max =100
min = 0
while guess!=999 :
    guess =eval(input("你猜多少(輸入999結束)?"))
    if guess == 999:
        break
    
    if guess >bomb :
        max = guess
        print("再小一些，",end=' ')
        print("請輸入{}~{}之間".format(min,max))
    elif guess <bomb :   
        min = guess
        print("再大一些",end=' ')
        print("請輸入{}~{}之間".format(min,max))
    else :
        print("恭喜破解密碼!")
         
print("你結束了這回合")