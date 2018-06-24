#E:\python\Ex_Files_Python_EssT\Practice python\listlessthan10.py

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = []

num = int(input('Please provide a number'))

for x in a: 
    if(x < num):
         new.append(x)

print(new)
