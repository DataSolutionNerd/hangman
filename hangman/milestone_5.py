from milestone_4 import Hangman

class milestone_5:
    
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
                game.ask_letter()
            elif game.num_lives != 0 and game.num_letters>0 :
                game.ask_letter()
            elif game.num_lives != 0 and game.num_letters <0 :
                print('Congratulations. You won the game!')
                break
            

    if __name__ == '__main__':
        word_list = ["apple", "spoon", "money", "green", "help"]
        play_game(word_list)




