import mysql.connector

#建立連線
connection = mysql.connector.connect(host = "localhost",
                                     port = "3307",
                                     user = "root",
                                     password = "steven408630852!",
                                     database = "firstbase")        #等同於『選擇資料庫』

#使用連線
cursor = connection.cursor()

#取得部門所有資料
cursor.execute("SELECT * FROM `branch`;")
record = cursor.fetchall()
for i in record:
    print(i)

cursor.close()
connection.close()