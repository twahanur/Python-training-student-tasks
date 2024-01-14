import sqlite3
db_students = sqlite3.connect('students.db')
db_students.execute('drop table if exists students')
db_students.execute(
    'create table students(roll int, name text, cls text, number text)')
db_students.execute('insert into students(roll, name, cls, number) values (?, ?, ?, ?)',
                    ("ROLL NO", 'NAME', 'CLASS', 'CONTACT NUMBER'))


def display_students():
    result = db_students.execute('select * from students')
    print("\n=== All Students ===")
    for student in result:
        print(student)
    print("====================")
    display()


def add_student():
    print("\n=== Add Student ===")
    roll = int(input('Enter student roll number: '))
    name = input('Enter student name: ')
    cls = input('Enter student class: ')
    number = input('Enter student contact number: ')

    db_students.execute('insert into students(roll, name, cls, number) values (?, ?, ?, ?)',
                        (roll, name, cls, number))
    db_students.commit()
    print("Student added successfully.")
    display()


def update_student():
    print("\n=== Update Student ===")
    roll = int(input('Enter student roll number: '))
    number = input('Enter updated contact number: ')
    db_students.execute(
        'update students set number=? where roll=?', (number, roll))
    db_students.commit()
    print("Student information updated successfully.")
    display()


def delete_student():
    print("\n=== Delete Student ===")
    roll = int(input('Enter student roll number to delete: '))
    db_students.execute('delete from students where roll=?', (roll,))
    db_students.commit()
    print("Student deleted successfully.")
    display()


def display():
    print("\n=== Student Management System ===")
    print('1. Show all students')
    print('2. Add student')
    print('3. Update student')
    print('4. Delete student')
    print('0. Exit')
    inp = int(input('Enter your choice: '))

    if inp == 1:
        display_students()
    elif inp == 2:
        add_student()
    elif inp == 3:
        update_student()
    elif inp == 4:
        delete_student()
    elif inp == 0:
        print("Exiting the program. Thank you!")
        return
    else:
        print("Invalid choice. Please try again.")
    display()


if __name__ == "__main__":
    display()
