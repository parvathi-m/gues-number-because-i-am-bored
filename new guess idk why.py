import random
guess = random.randint(1 , 9)
chances = 0
while chances < 5:
    number = int(input('Guess a number mere mortal, and it must be between 1 and 9 because yes'))
    if guess == number:
        print('your guess is correct and now i am sad')
        break
    elif guess > number:
        print('ha, your answer is wrong but u need to guess higher idk why im telling u this')
    elif guess < number:
        print('ha, your answer is wrong but u need to guess lower idk why im telling u this')
if not chances < 5:
    print('hahahh you lose, sucks to be you >:)')