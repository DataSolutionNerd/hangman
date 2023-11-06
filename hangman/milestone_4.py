# import libraries
import random as rd

class Hangman:
    # constructor
    def __init__(self, word_list):
        # initialise the attributes
        self.word_list = word_list
        self.num_lives = 5
        self.word = rd.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word)) - len(set(list(filter(lambda x: x != '_', self.word_guessed))))
        self.list_of_guesses = list()
        


