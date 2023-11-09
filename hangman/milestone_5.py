from milestone_4 import Hangman
class milestone_5:
    def play_game(word_list):
        num_lives = 5
        game = Hangman()
        game(word_list,num_lives)
        while True:
            if num_lives == 0:
                print('You lost!')
            if num_lives>0:
                game.ask_for_input()
            if num_lives != 0 and game.num_letters>0 :
                game.ask_for_input()
            if num_lives != 0 and game.num_letters <0 :
                print('Congratulations. You won the game!')


milestone_5.play_game()








