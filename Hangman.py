import random
import math
import string
import re

dictionary = ('vicious', 'type', 'tiger', 'yellow', 'strawberry', 'basketball', 'minute', 'mathematics', 'transporter', 'computer') 

chosen_word = random.choice(dictionary)
print(chosen_word)
chosen_word_len = len(chosen_word)

a = [""]*chosen_word_len
position = [0]*chosen_word_len
for i in range(chosen_word_len):
    a[i] = "____ "

    
print("\nGuess the word by guessing one letter at a time!")
letter = (input("Which letter would you like to guess?"))
print("The letter you guessed was " + (letter))
print((letter) + " was one of the letters in the word!")
'''guessed = re.findall(letter,chosen_word)
print(guessed)'''
for i in range(chosen_word_len):
    if (chosen_word[i]) == letter:
        a[i] = letter
        position[i] = 1
          
print(a)

for i in range(chosen_word_len):
    if(position[i] == 1):
        print("\"{}\" is in position {}!".format(letter, i+1))
        
        
    


