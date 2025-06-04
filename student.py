from db import connect
def student_menu(roll_no):
    while True:
        print("""\nstudent menu:
1.view details
2.view marks
3.view timetable
4.logout""")
        choice=input("enter choice: ")
        if choice=='1':
            view_details(roll_no)
        elif choice=='2':
            view_marks(roll_no)
        elif choice=='3':
            view_timetable(roll_no)
            print("logging out...")
            break
        else:
            print("invalid choice: ")
def view_details(roll_no):
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
    result = cur.fetchone()
    print(result)
    
    con.close()
view_details(1)
def view_marks(roll_no):
      con = connect()
      cur = con.cursor()
      cur.execute("SELECT subject,marks FROM marks where roll_no=101")
      for row in cur.fetchall():
          print(row)
      con.close()
student_menu(1)