#定義類別IO，有兩個屬性sup和read
class IO:
    sup = ["xxx", "yyy"]

    def read(src):
        if src not in IO.sup:
            print("NOT FOUND")
        else:
            print("read from " + src)

#呼叫

print(IO.sup)
IO.read("xxx")
IO.read("zzz")