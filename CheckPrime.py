num = int(input('Number : '))

boolean = True;

for x in range (2, num):
    if (num%x == 0 ):
        boolean = False
        break
    
if(boolean == True):
    print('Is Prime')
else:
    print('Is NOT Prime')
        

        
