import random

r = random.randint(1, 100)
while True:
    num = input('Please guess the number: ')
    num = int(num)
    if r == num:
        print('Finally, right!')
    else:
        print('The answer is:', r)
    break