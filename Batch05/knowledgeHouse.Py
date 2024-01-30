
import sqlite3

db = sqlite3.connect('knowledgeHouse.db')

db.execute('drop table if exists books')

db.execute('create table books(si int, name text,price int)')

db.execute('insert into books(si,name,price)values(?,?,?)',('si','name','price'))

db.execute('insert into books(si,name,price)values(?,?,?)',(12,'english',950))

db.execute('insert into books(si,name,price)values(?,?,?)',(13,'bangla',550))

db.execute('insert into books(si,name,price)values(?,?,?)',(14,'math',450))

db.execute('insert into books(si,name,price)values(?,?,?)',(15,'since',550))

db.execute('insert into books(si,name,price)values(?,?,?)',(16,'religion',650))

db.execute('insert into books(si,name,price)values(?,?,?)',(17,'ict',250))

db.execute('insert into books(si,name,price)values(?,?,?)',(18,'agricul',720))

db.execute('insert into books(si,name,price)values(?,?,?)',(19,'giografi',550))

db.execute('insert into books(si,name,price)values(?,?,?)',(20,'english',950))

db.execute('insert into books(si,name,price)values(?,?,?)',(14,'math',450))

db.execute('insert into books(si,name,price)values(?,?,?)',(15,'since',5589))

db.execute('insert into books(si,name,price)values(?,?,?)',(16,'religion',659))

db.execute('insert into books(si,name,price)values(?,?,?)',(17,'ict',255))

db.execute('insert into books(si,name,price)values(?,?,?)',(18,'agricul',720))

db.execute('insert into books(si,name,price)values(?,?,?)',(19,'giografi',550))

db.execute('insert into books(si,name,price)values(?,?,?)',(20,'english',12345))
db.commit()


def insertData():
    SI=int(input("enter books si:"))
    name=input("enter books name:")
    price=int(input("enter books price:"))
    db.execute('insert into books(si,name,price)values(?,?,?)',('si','name','price'))
    db.commit()
    print("Books Added Successfully")  


def displayData():
    data = db.execute('select * from books')
    for v in data :
        print (v)


def updateBooks():
    SI=int(input("enter books si:"))
    name=input("enter updeted name:")
    db.execute('updeted books sat price=? where si =?',(price,SI)) 


             
    db.commit()

def deleteBooks():
    SI=int(input("enter books si:"))
    db.execute('delete from books where si = ?',(SI))
    db.commit()
while(True):
    
    print("********WELCOME TO BOOKS ****************")
    print("******** 1.view all books************")
    print("********* 2.add books************")
    print("************ 3.update books***********")
    print("*************** 4.delete books*************")
    print("******************* 5.EXIT")
    choice=int(input("Enter your choice:"))
    if(choice == 1):
       
       displayData()
    
    elif(choice == 2):
        insertData()

    elif(choice == 3):
        updateBOOKS()
    
    
    elif(choice == 4):
        DeleteBooks()
    
    elif(choice == 5):
        break
    else:
        print("wrong input")
    
    
