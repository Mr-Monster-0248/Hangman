import security
import game
import os

choice = -1
errors = 0
win = False

#0 for ia
#1 for 2 player
game_mode = 0

print("#####################")
print("#      HANGMAN      #")
print("#####################")

while(choice != 1 and choice != 2):
    print("\nChoose your game mode")
    print("1 for 1 player")
    print("2 for 2 player")
    choice = security.input_choice()
