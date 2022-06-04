#ctrl + /(shift旁邊的)：多行註解/解除註解

#定義函式

def mul(n1, n2):
    print(n1 * n2)

def multiple(n1, n2):
    return n1 * n2
#呼叫函式

mul(3,4)
print(multiple(5,6))

value = multiple(2,3) + multiple(4,5)
print(value)

#程式的包裝

# sum = 0

# for n in range(1,11):
#     sum += n
# print(sum)

# sum = 0

# for n in range(1,21):
#     sum += n
# print(sum)

#上面兩個邏輯相似，可進行包裝，讓這個邏輯可以被重複利用

def culculate(max):
    sum = 0
    for n in range(1,max+1):
        sum += n
    print(sum)

culculate(10)
culculate(20)