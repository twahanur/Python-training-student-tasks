def add (x,y):
    return (x+y)
def subtract (x,y):
    return (x-y)
def Multiply (x,y):
    return (x*y)
def Divition (x,y):
    if y!=0:
        return x/y
    else:
        print("invalid input. try again...\n")
def calculator():
    print("***simple calculator***")


while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit")
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
    if choice == "5":
        print("Goodbye!")
        break 
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = Multiply(num1, num2)
    elif choice == "4":
        result = Divition(num1, num2)
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        continue
    print("Result:", result)
