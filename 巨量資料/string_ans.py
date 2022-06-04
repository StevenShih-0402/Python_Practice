# # Q1請串聯 ls 與 rs後印出
ls = "天地良心"
rs = "日月可鑒"
print(ls+"-"+rs)
# Q2請把s 重複3次印出
s = "戴口罩\n"
print(s*3)

# Q3 請印出:  這個句子有 ? 字
sentence = "勤洗手，戴口罩，保護自己，愛護家人"
print(len(sentence))
# Q4單字是否存在句子
n = "戴口罩"
sentence = "勤洗手，戴口罩，保護自己，愛護家人"
print("原始:",sentence)
is_in_sentenctc = n in sentence
print(is_in_sentenctc)
words = sentence.split("，")
print("分隔完:",words)
print(words[0])
print(words[1])
print(words[2])
print(words[3])
# Q5請把下面的變數轉成字串印出
lucky_num = 55688
print(str(lucky_num))
