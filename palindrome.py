myString = input('Input a string: ')

myStack = []

for eachLetter in myString:
    myStack.append(eachLetter)

#print(myStack)

myTempList = []

#print(len(myStack))

#string = str(myStack.pop())

#print(f'This is popping the first element of myStack {string}')

while(len(myStack) != 0):
    myTempList.append(myStack.pop())

#print(f'This is myTempList {myTempList}')

tempString = ''.join(str(elm) for elm in myTempList)
#print(tempString)

if(myString == tempString):
    print('Is a Palindrome')
else:
    print('Is not a palindrome')
    

