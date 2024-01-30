import sqlite3

db = sqlite3.connect('peace_of_belly.db')

db.execute('drop table if exists foods')

db.execute('create table foods(si int, name text,price int)')

db.execute('insert into foods(si,name,price) values(?,?,?)',
           ('si', 'name', 'price'))
db.execute('insert into foods(si,name,price) values(?,?,?)',
           (1, 'chess burger', 656))
db.execute('insert into foods(si,name,price) values(?,?,?)',
           (2, 'fruit custerd', 850))
db.execute('insert into foods(si,name,price) values(?,?,?)',
           (3, 'chiken fry', 995))
db.execute('insert into foods(si,name,price) values(?,?,?)', (4, 'pizza', 440))
db.execute('insert into foods(si,name,price) values(?,?,?)', (5, 'faluda', 220))
db.execute('insert into foods(si,name,price) values(?,?,?)',
           (6, 'chiken rol', 550))
db.execute('insert into foods(si,name,price) values(?,?,?)',
           (7, 'cold drinks', 35))
db.execute('insert into foods(si,name,price) values(?,?,?)',
           (8, 'black coffie', 150))
db.execute('insert into foods(si,name,price) values(?,?,?)',
           (9, 'kacci biriane', 550))
db.commit()


def addItem():
    si = int(input("enter item si:"))
    name = input("enter foods name: ")
    price = int(input("enter foods price: "))
    db.execute('insert into foods(si,name,price) values(?,?,?)',
               (si, name, price))
    db.commit()
    print("Item Added Succesfully")


def displayFoods():
    result = db.execute('select * from foods')
    for row in result:
        print(row)


def updatePrice():
    si = int(input("enter item si: "))
    price = int(input("enter foods price:"))
    db.execute('update foods set price=? where si = ?', (price, si))
    db.commit()


def deleteItem():
    si = int(input("enter item si : "))
    db.execute('delete from foods where si = ?', (si))
    db.commit()


while (True):
    print("*********Welcome To Peace_Of_Belly.db***********")
    print("  1. view all foods ")
    print("  2. add foods ")
    print("  3. update foods ")
    print(" 4. delete foods item ")
    print("  5. Exit ")
    choice = int(input("Enter your choice:  "))
    if (choice == 1):
        print("choice 1")
        displayFoods()
    elif (choice == 2):
        print("choice 2")
        addItem()
    elif (choice == 3):
        print("choice  3")
        updatePrice()
    elif (choice == 4):
        print("choice  4")
        deleteItem()
    elif (choice == 5):
        break
    else:
        print("wrong input")
