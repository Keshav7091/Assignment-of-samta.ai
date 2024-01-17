

import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", 
                      user="root",
                      password="851129",
                      auth_plugin='mysql_native_password')

db_cursor = mydb.cursor()

db_cursor.execute("create database smataAssign")

print("Database created !!")