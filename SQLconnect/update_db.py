import mysql.connector

#建立連線
connection = mysql.connector.connect(host = "localhost",
                                     port = "3307",
                                     user = "root",
                                     password = "steven408630852!",
                                     database = "firstbase")        #等同於『選擇資料庫』

#使用連線
cursor = connection.cursor()

# #新增
# cursor.execute("INSERT INTO `branch` VALUES(5, '打雜', NULL);")
# #修改
# cursor.execute("UPDATE `branch` SET `manager_id` = 209 WHERE `branch_id` = 5;")
# #刪除
# cursor.execute("DELETE FROM `branch` WHERE `branch_id` = 5;")

cursor.close()
connection.commit()     #將修改資料的指令提交出去
connection.close()