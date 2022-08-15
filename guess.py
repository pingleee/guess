import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = input('Please guess the number: ')
    num = int(num)
    if r == num:
        print('Finally, right!')
        break
    elif num > r:
        print('Too Big.')
    else :
        print('Too Small.')
    print('You guess', count, 'times')