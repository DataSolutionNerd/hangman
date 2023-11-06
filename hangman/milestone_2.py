# import random
import random as rd
# import random for string of alphabet
import string

# Task 1
# List containing the names of my 5 favourite fruits
word_list = ['strawberry', 'kiwi', 'grapes', 'banana', 'orange']
# Print out the created list
print(word_list)

# Task 2
word = rd.choice(word_list)
print(word) 

# Task 3
print("Please enter a single letter input: ")
guess = input()

# Task 4
if len(guess) == 1 and guess.lower() in list(string.ascii_lowercase):
    print("Good guess")
else:
    print("Oops! That is not a valid input.")