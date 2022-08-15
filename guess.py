import random

r = random.randint(1, 100)
t = 1
while True:
    num = input('Please guess the number: ')
    num = int(num)
    if r == num:
        print('You guess', t ,'times. Finally, right!')
        break
    else:
        print('You guess', t ,'times. Wrong!')
    t = t + 1