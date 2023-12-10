import random

a = random.randint(1, 5)

print("Welcome to the Number Guessing Game!")

while True:
    gues = int(input("Enter your guess (between 1 and 5): "))
    if gues < r:
        print("Too low! Try a greater number.")
    elif gues > r:
        print("Too high! Try a smaller number.")
    else:
        print(f"Congratulations! You guessed the correct number, {a}!")
        break
