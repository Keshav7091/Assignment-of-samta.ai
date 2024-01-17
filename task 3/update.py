import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", 
                      user="root",
                      password="851129",
                      auth_plugin='mysql_native_password',
                      database="smataassign")

db_cursor = mydb.cursor()

update_query = """
UPDATE students1
SET grade = 97.0
WHERE first_name = 'Alice'
"""
db_cursor.execute(update_query)
mydb.commit()