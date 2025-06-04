''''
admin features:
1.add student
2.delete student
3.update student
4.time table
5.marks

'''
from db import connect
def admin():
    conn=connect()
    cursor=conn.cursor()
    print("""\nadmin menu:
    1.add student
    2.update student details
    3.reset student password
    4.update marks
    5.view all students
    6.update timetable
    7.logout""")
    ch=int(input("enter your choice: "))
    if ch==1:
        add_student()
    elif ch==2:
        update_student()
    elif ch==3:
        rest_student_password()
    elif ch==4:
        update_marks()
    elif ch==5:
        view_all_students()
    elif ch==6:
        update_timetable
    elif ch==7:
        logout()
    else:
        print("invalid choice. please try again.")
def add_student():
    con=connect()
    cursor=con.cursor()
    roll_no=input("enter roll no: ")
    name=input("enter name: ")
    class_name=input("enter class: ")
    section=input("enter section: ")
    password="password@123"
    email=input("enter email: ")
    query="insert into students (roll_no,name,class,section,password,email) values(%s,%s,%s,%s,%s,%s)"
    values=(roll_no,name,class_name,section,password,email)
    cursor.execute(query,values)
    con.commit()
    print("student added successfully.")
def update_student():
    con=connect()
    cursor=con.cursor()
    roll_no = input("Enter Roll No of student to update: ")
    name = input("Enter new name: ")
    class_name = input("Enter new class: ")
    section = input("Enter new section: ")
    email = input("Enter new Email: ")
    query="UPDATE students SET name=%s, class=%s, section=%s, email=%s, roll_no=%s"
    values = (name, class_name, section, email, roll_no)
    cursor.execute(query, values)
    con.commit()
    print("student details updated sucessfully")
def reset_student_password():
    pass
def update_marks():
    con=connect()
    cursor=con.cursor()
    roll_no = input("Enter roll_no of student to update marks")
    subject = input("Enter Subject: ")
    marks = input("Enter Marks: ")
    query = "UPDATE marks SET marks=%s WHERE roll_no=%s AND subject=%s"
    values = (marks, roll_no, subject)
    cursor.execute(query,values)
    con.commit()
    print("Marks updated sucessfully.")
def view_all_students():
    con=connect()
    cursor=con.cursor()
    query="SELECT * FROM students"
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)
def update_timetable():
    pass
def logout():
    print("logging out....")
    # here you can add any additional logout logic if need
    return
#example usage
if __name__=="__main__":
    admin()