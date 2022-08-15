import random

minn = input('Please enter the min: ')
maxx = input('Please enter the max: ')
minn = int(minn)
maxx = int(maxx)
r = random.randint(minn, maxx)
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