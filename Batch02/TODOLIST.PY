import sqlite3

db = sqlite3.connect('ToDoList.db')

db.execute('DROP TABLE IF EXISTS ToDoList')

db.execute('''
    CREATE TABLE ToDoList (
        serialNo INTEGER,
        taskName TEXT
    )
''')

serial = 1


def addToList(task):
    global serial
    print(f"Adding task: {task}")
    db.execute(
        "INSERT INTO ToDoList (serialNo, taskName) VALUES (?, ?)", (serial, task))
    db.commit()
    serial += 1


def updateList(serial, task):
    print(f"Updating task {serial}: {task}")
    db.execute("UPDATE ToDoList SET taskName=? WHERE serialNo=?", (task, serial))
    db.commit()


def deleteFromList(serial):
    print(f"Deleting task: {serial}")
    db.execute("DELETE FROM ToDoList WHERE serialNo=?", (serial))
    db.commit()


def showList():
    print("Showing tasks:")
    data = db.execute('SELECT * FROM ToDoList')
    for row in data:
        print(row)


addToList('breakfast')
addToList('reading books')
addToList('doing homework')
addToList('cleaning room')
addToList('watching TV')
addToList('eating apple')
addToList('going to market')
addToList('playing football')
addToList('wake up morning')

showList()

updateList(3, "take a nap")

showList()

deleteFromList(5)
showList()
