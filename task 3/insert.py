import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", 
                      user="root",
                      password="851129",
                      auth_plugin='mysql_native_password',
                      database="smataassign")

db_cursor = mydb.cursor()

insert_query = """
INSERT INTO students1 (first_name, last_name, age, grade)
VALUES ('Alice', 'Smith', 18, 95.5)
"""

db_cursor.execute(insert_query)

mydb.commit()
