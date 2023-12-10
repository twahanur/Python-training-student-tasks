import sqlite3

db = sqlite3.connect("students_database.db")

db.execute('''
    CREATE TABLE IF NOT EXISTS studentdatabase (
        student_roll INTEGER,
        student_name TEXT,
        student_class INTEGER,
        student_contact TEXT
    )
''')


def addtodo(r, n, cls, contact):
    print(f"Adding student: {n}")
    db.execute("INSERT INTO studentdatabase (student_roll, student_name, student_class, student_contact) VALUES (?, ?, ?, ?)", (r, n, cls, contact))
    db.commit()


def updatedb(r, n):
    print(f"Updating student name for roll {r}")
    db.execute(
        "UPDATE studentdatabase SET student_name=? WHERE student_roll=?", (n, r))
    db.commit()


def deletefromdb(r):
    print(f"Deleting student with roll {r}")
    db.execute("DELETE FROM studentdatabase WHERE student_roll=?", (r,))
    db.commit()


def studentdisplaydb():
    data = db.execute("SELECT * FROM studentdatabase")
    print("total students list from database")
    for row in data:
        print(row)


addtodo(28, 'Shawon Ghosh', 7, '013624474751')
addtodo(24, 'Rakib', 7, '01316541341')
addtodo(4, 'rudro', 6, '01325746164')
addtodo(5, 'animika', 6, '0121631354')
addtodo(77, 'aritro', 7, '0113431343')
addtodo(71, 'Es Das', 6, '1020484041316')
addtodo(7, 'talha', 6, '01225412451')
addtodo(70, 'talha', 6, '01225412451')

studentdisplaydb()

updatedb(71, 'Porosh')
studentdisplaydb()

deletefromdb(70)
studentdisplaydb()
