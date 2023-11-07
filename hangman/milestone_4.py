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
        

    def check_guess(self, guess):
        if guess.lower() in list(self.word):
            print("Good guess! {guess} is in the word.")
            for x  in list(self.word):
                position = 0
                if x.lower == guess.lower():
                    self.word_guessed[position].replace("_", guess)
                    position = position+1
                else:
                    continue
        else:
            print("Oh no! {guess} is not in the word.")

        self.num_letters = self.num_letters- 1






    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                mileston_four.check_guess(guess)
                self.list_of_guesses.append(guess)
                

# Test Code 
secret_word = ("apple", "spoon", "easy", "sown", "help")
mileston_four = Hangman(secret_word)
mileston_four.ask_for_input()
  





