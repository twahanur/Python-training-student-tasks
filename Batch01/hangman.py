import random

def hangman():
    print("************************* Welcome to Hangman! ****************************\n")
    collection =['book','cat','dog','cow','orange','cycle','laptop','character']
    x = random.choice(collection)
    print(x)
    while True:
        guess = input('guess the word first letter of '+x[0]+':').lower()
        if(x==guess):
            print('wow!you got it')
            break
        else:
            print('you put the wrong answer.please try again')

hangman()
