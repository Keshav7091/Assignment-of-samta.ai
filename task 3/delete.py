import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", 
                      user="root",
                      password="851129",
                      auth_plugin='mysql_native_password',
                      database="smataassign")

db_cursor = mydb.cursor()



delete_query = """
DELETE FROM students1
WHERE last_name = 'Smith'
"""
db_cursor.execute(delete_query)
mydb.commit()

print("delete query")

