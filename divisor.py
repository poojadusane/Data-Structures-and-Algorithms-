num = int(input('num: '))

newList = []
for x in range (1, num):
    if(num%x == 0):
        newList.append(x)


print(newList)