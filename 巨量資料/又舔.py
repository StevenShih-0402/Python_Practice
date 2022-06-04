# 題目來源: https://forum.gamer.com.tw/C.php?bsn=60076&snA=6702822&tnum=6

while(True):
    tt = str(input("又舔嘴唇！"))
    if(len(tt) > 1000):
        print("叫殺小啦！")
        continue
    if(tt == '一代一代'):
        print("啊！一代一代一代！")
        break
    print(tt.count('tt'))

# 才華洋溢的範例
# def getcount(text):
#     return len(text.split("tt"))-1

# tt = str(input())
# print(getcount(tt))





