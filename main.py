import random

while (True):
    number = random.randrange(1,100,1)
    print("Guess the number between 1 and 100")

    choice = 0
    while (True):

        guess = int(input())

        if (guess == number):
            print("CORRECT !!!")
            break;

        elif (choice == 10):
            print("Ran out of choices")
            break

        elif (guess > number):
            print("Your Guess value is High")
            choice +=1

        elif (guess < number):
            print("Your Guess value is Low")
            choice +=1

    print("Do you want to play again ? y/n")
    x = input()

    if (x=='n' or x=='N' or x=='no' or x == 'NO'):
        break;

print("!!! THANK YOU !!!")
