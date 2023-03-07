import random
number = random.randrange(1, 100)
option = input("Enter yes/no to start or quit the game\n")
#Are you sure you are ready for the game
if str(option) == 'y' or str(option) == 'yes':
    #The conditional loop for the game
    guess = int(input("Enter a matching guess"))
    while True:
        if guess > number:
            guess = int(input("guess too high, Try again"))
        elif guess < number:
            guess = int(input("guess too low, Try again"))
        else:
            print("Guess correct, You've won the game")
            break
else:
    exit