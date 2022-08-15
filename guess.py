import random
start = input('Please enthr the Start range: ')
end = input('Please enter the End range: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
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