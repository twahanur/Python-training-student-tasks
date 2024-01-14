import sqlite3

db = sqlite3.connect('restaurant.db')
db.execute('drop table if exists restaurant')
db.execute(
    'create table restaurant(id int, food_name text, food_price int, food_type text)')
db.execute('insert into restaurant(id, food_name, food_price, food_type) values (?, ?, ?, ?)',
           ("FOOD ID", "FOOD NAME", "FOOD PRIZE", "FOOD TYPE"))


def display():
    print("\n=== Restaurant Management System ===")
    print('1. Show all items')
    print('2. Add item')
    print('3. Update item')
    print('4. Delete item')
    print('0. Exit')
    inp = int(input('Enter your choice: '))

    if inp == 1:
        display_all_data()
    elif inp == 2:
        add_item()
    elif inp == 3:
        update_item()
    elif inp == 4:
        delete_item()
    elif inp == 0:
        print("Exiting the program. Thank you!")
        return
    else:
        print("Invalid choice. Please try again.")
    display()


def display_all_data():
    result = db.execute('select * from restaurant')
    print("\n=== All Items ===")
    for i in result:
        print(i)
    print("=================")
    display()


def add_item():
    print("\n=== Add Item ===")
    food_id = int(input('Enter food id: '))
    price = int(input('Enter food price: '))
    food_type = input('Enter food type: ')
    name = input('Enter food name: ')

    db.execute('insert into restaurant(id, food_name, food_price, food_type) values (?, ?, ?, ?)',
               (food_id, name, price, food_type))
    db.commit()
    print("Item added successfully.")
    display()


def update_item():
    print("\n=== Update Item ===")
    food_id = int(input('Enter food id: '))
    food_price = int(input('Enter updated price: '))
    db.execute('update restaurant set food_price=? where id=?',
               (food_price, food_id))
    db.commit()
    print("Item updated successfully.")
    display()


def delete_item():
    print("\n=== Delete Item ===")
    food_id = int(input('Enter food id to delete: '))
    db.execute('delete from restaurant where id=?', (food_id,))
    db.commit()
    print("Item deleted successfully.")
    display()


if __name__ == "__main__":
    display()
