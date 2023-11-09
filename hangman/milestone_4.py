# import libraries
import random as rd

class Hangman:
    # constructor
    def __init__(self, word_list, num_lives ):
        # initialise the attributes
        self.word_list = word_list
        self.num_lives = 5
        self.word = rd.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        
    # def print_all_attributes(self):
       #  print(f'word_list: {self.word_list}, num_lives: {self.num_lives}, word: {self.word}, word_guessed: {self.word_guessed}, num_letters: {self.num_letters}, list_of_guesses: {self.list_of_guesses}')

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in list(self.word):
            self.num_letters = self.num_letters- 1  
            for i, x in enumerate(self.word):
                if x == guess:
                    self.word_guessed[i] = x
            print(f"Good guess! {guess} is in the word.")
            print(f"{self.word_guessed}")
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            print(f"{self.word_guessed}")
        


    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print(f"You already tried the letter {guess}!")
                self.list_of_guesses.append(guess)
                continue
            else:
                #self.list_of_guesses.append(guess)
                self.check_guess(guess)
            break
       
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif '_' not in game.word_guessed:
            print('Congratulations. You won the game!')
            break
        elif game.num_lives>0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters>0 :
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters <0 :
            print('Congratulations. You won the game!')
            break
        

if __name__ == '__main__':
    word_list = ["apple", "spoon", "money", "green", "help"]
    play_game(word_list)
        
        
