# import libraries
import random

# Task 1: Iteratively check if input is valid

while True:
    guess = input("Guess a letter: ")
    if len(guess)== 1 and guess.isalpha():
        letter = guess
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        continue


# Task 2: check weather the guess is in the word

secret_word = ("apple", "spoon", "easy", "sown", "help")
random_word = random.choice(secret_word)

if guess in list(random_word):
    print(f'Good guess! {guess} is in the word.')
else:
    print(f'Sorry, {guess} is not in the word. Try again.')
            
