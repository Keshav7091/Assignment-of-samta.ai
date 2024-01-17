import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", 
                      user="root",
                      password="851129",
                      auth_plugin='mysql_native_password',
                      database="smataassign")

db_cursor = mydb.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS students1 (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    grade decimal()
)
"""

db_cursor.execute(create_table_query)

print("Table Created!!")