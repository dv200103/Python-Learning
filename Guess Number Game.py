#This is a guess a game number.
import random
secretNumber = random.randint(1,20)
print('I am thinking a number between 1 and 20.')

# Ask a player to guess 6 time.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break    #This condition is correct guess


if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
