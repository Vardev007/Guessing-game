#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random  #here imporing librabry function for using import function


# Now the pc is going to select a random variable from given range
num = random.randint(1,100) 


print('__________________WELCOME______________________')
print('________________GUESSING_GAME__________________')
print('___________GUESS A NUMBER BETWEEN 0-100________')


#this is basically will count the number of guess we made during the game to find the number
guesses = [0]




while True:
    
    #taking input from the user and placing it in guess every time they guess a number
    guess = int(input('What do you think it is ? \n'))
    
    
    #comparing the guess made by user looking if it was in the range we made
    if guess<1 or guess>100:
        print('Select numbers from only 1-100')
        continue
        
    #now if the user guess it correctly then its done  
    if guess == num:
        print(f'You Got It Baby !!!  You Made It in  {len(guesses)} guesses only')
        break
        
    #counting number of guesses made by user    
    guesses.append(guess) 
    
    #Comparing guess and number made by user
    if guess < num:
        print(f'Greater than {guess}')
        
    else:
        print(f'Is Less than {guess}')


# In[ ]:




