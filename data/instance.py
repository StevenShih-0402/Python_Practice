class Point:
    
    #實體物件(相當於JAVA的建構式)
    # def __init__(self):
    #     self.x = 3
    #     self.y = 4
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #實體方法
    def show(self):
        print(self.x, self.y)

    def distance(self, tarX, tarY):
        return (((self.x - tarX)**2) + ((self.y - tarY)**2))**0.5

#建立實體物件
# p1 = Point()
p2 = Point(5,12)

#取得實體資料
# print(p1.x, p1.y)
print(p2.x, p2.y)

#呼叫實體方法
p2.show()
result = p2.distance(0,0)
print(result)

#案例：File

class File:
    def __init__(self, name):
        self.name = name
        self.file = None
    
    def open(self):
        self.file = open(self.name, mode = "r", encoding = "utf-8")
    
    def read(self):
        return self.file.read()

f1 = File("data1.txt")
f1.open()
data = f1.read()
print(data)

f2 = File("data2.txt")
f2.open()
data = f2.read()
print(data)