#this is a basic number guessing game
import random

count = 0 ##this is the counter for the game, which ticks up per each guess
answer = random.randint(0, 20) ##this is the answer, obviously
acceptable = 0 ##this is a flag to break the while loop for input
guess = 0 ##this is the guess that player offers

## let the games begin
print('I\'ve guessed a number from 0-20, now you better find it or else.')
for rounds in range(6):
    print('Round #',str(count+1))
    guess = input('What\'s your guess?\n')
    try: ##this try block is the actual handling of the guess, the rest is input validation and retry
        guess = int(guess)
        if guess>=0 and guess<=20:
            if guess == answer:
                print('You win!')
                break
            elif guess > answer:
                print('Your guess is too high')
                count +=1 
            elif guess < answer:
                print('Your guess is too low.')
                count +=1
        else:
            print('You wasted a turn on a number that isn\'t in range and it is pathetic.')
            count +=1
    except:
        acceptable=0
        while (acceptable==0):
            acceptable=0
            print('You have not entered a number and that\'s a problem.')
            guess = input('What\'s your guess for real?\n')
            try:
                guess = int(guess)
                acceptable=1
                if guess>=0 and guess<=20:
                    if guess == answer:
                        print('You win!')
                        break
                    elif guess > answer:
                        print('Your guess is too high')
                        count +=1 
                    elif guess < answer:
                        print('Your guess is too low.')
                        count +=1
                else:
                    print('You wasted a turn on a number that isn\'t in range and it is pathetic.')
                    count +=1
            except:
                print('Please try harder.')
