import sqlite3
db = sqlite3.connect("school.db")
db.execute('drop table if exists student')
db.execute('create table student(id int, name text, class int)')
db.execute('insert into student(id,name,class) values(?,?,?)',("ID","NAME","CLASS"))
db.execute('insert into student(id,name,class) values(?,?,?)',(1,"amir",5))
db.execute('insert into student(id,name,class) values(?,?,?)',(2,"amir",6))
db.execute('insert into student(id,name,class) values(?,?,?)',(3,"amir",6))
db.execute('insert into student(id,name,class) values(?,?,?)',(4,"amir",8))
db.execute('insert into student(id,name,class) values(?,?,?)',(5,"amir",9))
db.commit()
def insertData():
    ID = int(input("enter student id: "))
    name = input("enter student name: ")
    cls = int(input("enter student class: "))
    db.execute('insert into student(id,name,class) values(?,?,?)',(ID,name,cls))
    db.commit()
    print("Student Added Successfully")

def displayData():
    data = db.execute("select * from student")
    for v in data:
        print(v)

def updateStudent():       
    ID = int(input("enter student id: "))
    cls = int(input("enter updated class: "))
    db.execute('update student set class=? where id = ?',(cls,ID))
    db.commit()
def deleteStudent():
    ID = int(input("enter student id: "))
    db.execute('delete from student where id = ?',(ID))
    db.commit()

while(True):
    print("*************** WELLCOME TO STUDENT DASHBORD ***************")
    print("* 1. view all students")
    print("* 2. add student")
    print("* 3. update student")
    print("* 4. Delete Student")
    print("* 5. EXIT")
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        displayData()
    elif(choice == 2):
        insertData()
    elif(choice == 3):
        updateStudent()
    elif(choice == 4):
        deleteStudent()
    elif(choice == 5):
        break
    else:
        print("Wrong input")

















