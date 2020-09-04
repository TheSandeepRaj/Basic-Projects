# This is a guess the number game.
# The REAL ONE
import random

def GuessTheNumber(guess):
    if guess == secrectNumber:
        print("Congratulations! You've guessed it right.")
    elif guess < secrectNumber:
        print('Your guess is too low.')    
    else:
        print("Your guess is too high")

print('Hi! What is your name?')
name = input()

print('\nWell, ' + name + '. Would you like to play "Guess The Number". \nAnswer in "Yes" or "No".\n')
answer = input()

if answer.lower() == 'yes':
    print('Hey ' + name + ' Welcome to "Guess The Number" game.' + "\nI'm thinking of number between 1 to 20")

    secrectNumber = random.randint(1, 20)

    for guessTaken in range(1,7):          #for only run 6 times
        print("\nTake a guess.")
        guess = input()
        if guess.isdigit() and (0 < int(guess) < 21):       # to check is guess in int and in given range
            guess = int(guess)                      # input takes guess in < class 'str' > though it is int rignt?
            GuessTheNumber(guess)
        else:
            print('Sorry, you have to choose number between 1 to 20')
    if guess == secrectNumber:
        print('You took '+ str(guessTaken) + ' guesses so far.')
    else:
        print('\nActually I was thinking of number ' + str(secrectNumber) + '.')

elif answer.lower() == 'no':
    print('Okay, thanks for checking in :), Bye for now.')

else:
    print('I take that as No, Bye for now.')
