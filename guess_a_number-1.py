import random
print('Let\'s guess a number!.')

num = random.randint(1, 100)
count = 0

while True:
    guess = int(input('Guess a number from 1 to 100: '))
    if guess > num:
        count += 1
        print('Guess smaller.')
    elif guess < num:
        count += 1
        print('Guess bigger.')
    else:
        count += 1
        print('Congrats! The number is %d.' % num)
        if count == 1:
            print('You took 1 try to reach to the correct number.')
        print('You took %d tries to reach to the number.' % count)
        break
