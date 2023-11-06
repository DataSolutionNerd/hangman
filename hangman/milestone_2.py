# import random
import random as rd
# import random for string of alphabet
import string
class Mileston_Two:
    # Constructor
    def __init__(self, word_list = list()):
        self.word_list = word_list
        self.guess = input("Type here: ")

    # Task 1
    def show_fruits(self):
        print(self.word_list)

    # Task 2
    def pick_fruit(self):
        word = rd.choice(self.word_list)
        print(word) 


    def enter_letter_input(self):
        # Task 3
        print("Please enter a single letter input")
        self.guess
        # Task 4
        if len(self.guess) == 1 and self.guess.lower() in list(string.ascii_lowercase):
            print("Good guess")
        else:
            print("Oops! That is not a valid input.")



# List containing the names of my 5 favourite fruits
word_list = ['strawberry', 'kiwi', 'grapes', 'banana', 'orange']
# Create an instance
milestone_tasks = Mileston_Two(word_list)
# Task 1: Print out the created list
milestone_tasks.show_fruits()
# Task 2: pick a random fruit
milestone_tasks.pick_fruit()
# Task 3 and 4: check if input is letter from alphabetk
milestone_tasks.enter_letter_input()


