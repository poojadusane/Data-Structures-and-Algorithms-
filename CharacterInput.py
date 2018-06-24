name = input('what is your name?')

age = int(input('what is your age'))

yr100th = 2018 - age + 100
    
print (f'Your Name is {name}')

y = f'Year when you will be 100 years is {yr100th}'
print(y)

numOfCopies = int(input('How many times you want this to be printed?'))
print(numOfCopies * y, sep = '\n')
