num = int(input('given number:'))

if(num%2 == 0):
    print(f'{num} is Even')
elif(num%2 == 1):
    print(f'{num} is Odd')
if(num%4 == 0):
    print(f'The number is multiple of 4')

num2 = int(input('Divident'))
div = int(input('Divisor'))

if(num2%div == 0):
    print(f'{num2} is divided by {div}')
else:
    print(f'{num2} is NOT divided by {div}')
    
#E:\python\Ex_Files_Python_EssT\Practice python\OddOrEven.py