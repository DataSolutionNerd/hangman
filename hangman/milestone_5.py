import milestone_4

class milestone_5:
    
    def play_game(word_list):
        num_lives = 5
        game = milestone_4.Hangman(word_list, num_lives)
        while True:
            if num_lives == 0:
                print('You lost!')
                break
            elif num_lives>0:
                game.ask_for_input()
            elif num_lives != 0 and game.num_letters>0 :
                game.ask_for_input()
            elif num_lives != 0 and game.num_letters <0 :
                print('Congratulations. You won the game!')
                break


# Test Code 
word_list = ["apple", "spoon", "easy", "sown", "help"]

game_start = milestone_5()
game_start.play_game(word_list)

# Test Code 
# secret_word = ["apple", "spoon", "easy", "sown", "help"]
# mileston_four = Hangman(secret_word)
# mileston_four.print_all_attributes()
# ileston_four.ask_for_input()






