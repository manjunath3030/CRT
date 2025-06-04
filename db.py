
import mysql.connector
def connect():
    conn= mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dinesh 9618",
        database="student_management"
    )
    return conn
if(connect()):
    print("connection established succesfully")
else:
    print("connection failed")