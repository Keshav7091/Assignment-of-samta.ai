import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", 
                      user="root",
                      password="851129",
                      auth_plugin='mysql_native_password',
                      database="smataassign")

db_cursor = mydb.cursor()


select_query = "SELECT * FROM students1"
db_cursor.execute(select_query)
students = db_cursor.fetchall()

print("Student Records:")
for student in students:
    print(student)

# Close the cursor and database connection
db_cursor.close()
mydb.close()