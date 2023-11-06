# Task 1: Iteratively check if input is valid
def checks():
    while True:
        guess = input("Guess a letter: ")
        if len(guess)== 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue
    return guess

checks()