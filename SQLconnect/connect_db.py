import mysql.connector

#建立連線
connection = mysql.connector.connect(host = "localhost",
                                     port = "3307",
                                     user = "root",
                                     password = "steven408630852!")

#使用連線
cursor = connection.cursor()

#創建資料庫
# cursor.execute("CREATE DATABASE `pyTest`;")

#取得所有資料庫名稱
# cursor.execute("SHOW DATABASES;")
# record = cursor.fetchall()
# for i in record:
#     print(i)

#選擇資料庫
# cursor.execute("USE `firstbase`;")

#創建資料表
# cursor.execute("CREATE TABLE `qq`(qq INT);")

#關閉資料庫與連線
cursor.close()
connection.close()
