input1 = str(input('Player one: '))
input2 = str(input('Player two: '))

if (input1 == input2): print('Its a tie')
elif (input1 == 'rock' and input2 == 'paper'): print('player 2 wins')
elif (input1 == 'rock' and input2 == 'scissors'): print('player 1 wins')
elif (input1 == 'paper' and input2 == 'rock'): print('player 1 wins')
elif (input1 == 'paper' and input2 == 'scissors'): print('player 2 wins')
elif (input1 == 'scissors' and input2 == 'rock'): print('player 2 wins')
elif (input1 == 'scissors' and input2 == 'paper'): print('player 2 wins')
else: print('Invalid output')

    
        