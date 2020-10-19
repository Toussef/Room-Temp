# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:33:14 2020

@author: Youssef
"""

# Refer to README for details
print('Answer with Yes or no when needed. Capital Y please :D')
iTemp = float(input('What is the current temperature of the room?\n'))

while iTemp<24:
    answer = input('Would you like to raise the temperature?\n')
    if answer == 'Yes':
        answer = input('Would you like to raise it to 24 C?\n')
        if answer == 'Yes':
            print('That is optimal')
            break
        else:
            iTemp = float(input('Insert your new temperature:\n'))
    else:
        print("As you wish!")
        break 
        
    
while iTemp>24:
    answer = input('Would you like to lower it?\n')
    if answer == 'Yes':
        fTemp = float(input('Insert the desired temperature:\n'))
        
        if fTemp> iTemp:
            print('You must enjoy the heat!')
        elif fTemp == 24:
            print("That is optimal!")
            break
        elif fTemp<24:
           answer = input('Would you like to raise it to the optimal temperature?\n')
           if answer == 'Yes':
               print('You are a smart person!')
               break
           else:    
               print('You must enjoy the chill!')
               break
    else:
        print("As you'd like!")
        break
            