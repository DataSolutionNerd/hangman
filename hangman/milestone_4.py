# import libraries
import random as rd

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
        
    list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
 
    '''
    # constructor
    def __init__(self, word_list, num_lives ):       
        # initialise the attributes
        self.word_list = word_list
        self.num_lives = 5
        self.word = rd.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        print(f'It is a {len(self.word_guessed)} letter word')
        print(self.word_guessed)
        
    # def print_all_attributes(self):
       #  print(f'word_list: {self.word_list}, num_lives: {self.num_lives}, word: {self.word}, word_guessed: {self.word_guessed}, num_letters: {self.num_letters}, list_of_guesses: {self.list_of_guesses}')

    def check_letter(self, letter):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        letter = letter.lower()
        if letter in list(self.word):
            self.num_letters = self.num_letters- 1  
            for i, x in enumerate(self.word):
                if x == letter:
                    self.word_guessed[i] = x
            print(f"Good guess! {letter} is in the word.")
            print(f"{self.word_guessed}")
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            print(f"{self.word_guessed}")
        


    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character and is a alphabet
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print(f"You already tried the letter {guess}!")
                continue
            else:
                self.list_of_guesses.append(guess)
                self.check_letter(guess)
            break
 