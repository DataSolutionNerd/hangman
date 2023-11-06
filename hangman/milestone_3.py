# import libraries
import random
# Milestone_3: Task 3
# Check weather the guess is in the word
def check_guess(guess):
    guess = guess.lower()
    secret_word = ("apple", "spoon", "easy", "sown", "help")
    random_word = random.choice(secret_word)
    if guess in list(random_word):
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
                
guess = input("Guess a letter: ")
check_guess(guess)


# Iteratively check if input is valid and check if the input letter is in the random word
def ask_for_input():
     while True:
        guess = input("Guess a letter: ")
        if len(guess)== 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue

# Call function
ask_for_input()


