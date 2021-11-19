import random

computer_win = 0
user_win = 0

choice = ['rock','paper','scissor']
while True:
    user_pick = input('\nPlease type Rock/Paper/Scissor or q to quit: ').lower()
    if user_pick == 'q':
        print('Thank you')
        quit()
    
    if user_pick not in choice:
        continue
    
    computer_pick = random.randint(0,2)
    # rock = 0  paper = 1   scissor = 2
    
    print('\nComputer picked',choice[computer_pick])
    
    if user_pick == choice[computer_pick]:
        print('Its a draw')
        continue
    
    if user_pick == 'rock' and computer_pick == 2:
        print('\nYou win!')
        user_win += 1
    
    elif user_pick == 'paper' and computer_pick == 0:
        print('\nYou win!')
        user_win += 1
        
    elif user_pick == 'scissor' and computer_pick == 1:
        print('\nYou win!')
        user_win += 1
        
    else:
        print('\nYou lost!')
        computer_win += 1
        
        
    
    
    
        
    play = input('\nDo you want to keep playing? (y/n):').lower()
    if play == 'y':
        continue
    
    else:
        break
    
print('\nYou win',user_win,'times')
print('The computer win',computer_win,'times')   
print('\nGoodbye!') 