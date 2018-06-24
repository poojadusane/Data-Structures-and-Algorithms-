import random

num = random.randint(1,9)

guestNum = int(input('Please input the number'))

if(guestNum > num):
    print('you guessed too high')
elif(guestNum < num):
    print('you guessed too low')
elif(guestNum == num):
    print('Bravo!! you guessed it exact same')
else:
    print('Invalid input')