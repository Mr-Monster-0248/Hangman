import security
import game
import draw
from os import system

choice = -1
errors = 0
win = False

#1 for ia
#2 for 2 player
game_mode = 0
secret_w = ""
player_w = ""
gessed = [" "]

system("clear")
print("#####################")
print("#      HANGMAN      #")
print("#####################")

while(game_mode != 1 and game_mode != 2):
    print("\nChoose your game mode")
    print("1 for 1 player")
    print("2 for 2 player")
    game_mode = security.input_choice()

system("clear")
if(game_mode == 1): #One player mode
    secret_w = game.choose_word_ia()
    while(game.word_diff(secret_w, player_w) and errors < 6):
        print("Letter you have gessed: ")
        print(" ".join(gessed))
        print("You have the right to make up to {} errors\n".format(6 - errors))

        draw.disp_hang(errors)
        player_w = game.initialize_player_w(secret_w, gessed)
        print(player_w)

        gess = " "
        while(gess in gessed):
            gess = security.input_char("Your gess: ")
        gessed.append(gess)
        if(not(gess in secret_w)):
            errors += 1
        player_w = game.initialize_player_w(secret_w, gessed)
        system("clear")

    if(not game.word_diff(secret_w, player_w)):
        print(player_w)
        print("You win !!")
    else:
        draw.disp_hang(errors)
        print("Sorry... whant to try again ?")


elif(game_mode == 2):
    print("work in progress")
