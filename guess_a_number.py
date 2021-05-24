import random

print('Let\'s guess a number.')

num = random.randint(1, 100)
count = 3
sum = 1

while True:
    if count != 0:
        guess = int(input('You have %d times to try. \nGuess a number: ' % count))
        if guess > num:
            count -= 1
            sum += 1
            print('Wrong. Guess smaller.')
        elif guess < num:
            count -= 1
            sum += 1
            print('Wrong. Guess bigger.')
        else:
            print('Congrats! You did it!')
            if count == 3:
                print('You gave 1 try to reach to the right number.')
            else:
                print('You gave %d tries to reach to the right number.' % sum)
            break
    else:
        print('BOOM! You failed to guess the right number.')
        print('The number is %d.' % num)
        break