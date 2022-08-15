import random

r = random.randint(1, 100)
t = 1
while True:
    num = input('Please guess the number: ')
    num = int(num)
    if r == num:
        print('You guess', t ,'times. Finally, right!')
        break
    elif num > r:
        print('You guess', t ,'times. Too Big.')
    else :
        print('You guess', t ,'times. Too Small.')
    t = t + 1