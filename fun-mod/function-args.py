#參數的預設資料

def power(base, exp = 0):
    print(base ** exp)


power(2, 3)
power(4)

#參數名稱對應

def devide(n1, n2):
    print(n1 / n2)

devide(4, 2)
devide(n2 = 3, n1 = 12)

#無限參數

def infinite(*ele):
    for x in ele:
        print(x)

infinite(3,4,5)
infinite("ahoy", "rody", "aaaaaa", "charrrrrge")