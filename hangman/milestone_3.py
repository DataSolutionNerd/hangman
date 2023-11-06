# import libraries
# import libraries 
import random

# Milestone_3: Task 3
# Check weather the guess is in the word
def check_guess_in_word(guess):
    guess = guess.lower()
    secret_word = ("apple", "spoon", "easy", "sown", "help")
    random_word = random.choice(secret_word)
    if guess in list(random_word):
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
                

# Iteratively check if input is valid and check if the input letter is in the random word
def check_input_validity_n_guess():
     # while loop
     while True:
        guess = input("Guess a letter: ")
        if len(guess)== 1 and guess.isalpha():
            # Check the valid letter is in the word
            check_guess_in_word(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue

# Call function
check_input_validity_n_guess()



