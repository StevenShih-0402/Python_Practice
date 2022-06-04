#數字運算
x = 7//6   #整數除法
x = 6/3    #正常除法
x = 2 * 3  #乘法
x = 2 ** 3 #平方

#字串運算
s = "\"hello\"~"  #\：跳脫字元
print(s)

s = "hello""world"
print(s)

#意同"hello\nworld\nyoho~"
s = """hello
world
yoho~"""
print(s)

#字串乘法和加法
s = "hello" * 3 + "world"
print(s)

#字串索引
s = "hello"
print(s[0])
print(s[1:3])  #包含開頭不包含結尾
print(s[1:])   #不給結尾→從起點到最後
print(s[:4])   #只給結尾→從最初到終點