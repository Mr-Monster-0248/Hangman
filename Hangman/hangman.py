import security
import game
import draw

play = True
while(play):
    errors = 0
    #1 for ia
    #2 for 2 player
    game_mode = 0
    secret_w = ""
    player_w = ""
    gessed = [" "]
    gender = -1

    security.clear()
    print("#####################")
    print("#      HANGMAN      #")
    print("#####################")

    while(game_mode != 1 and game_mode != 2):
        print("\nChoose your game mode")
        print("1 for 1 player")
        print("2 for 2 player")
        game_mode = security.input_choice()

    while(gender != 1 and gender != 2):
        print("\nChoose how you want to be portray")
        print("1 for man")
        print("2 for woman")
        gender = security.input_choice()

    if(game_mode == 1): #One player mode
        secret_w = game.choose_word_ia()
    elif(game_mode == 2):
        secret_w = game.choose_word_player()

    security.clear()

    while(game.word_diff(secret_w, player_w) and errors < 6):
        print("Letter you have gessed: ")
        print(" ".join(gessed))
        print("You have the right to make up to {} errors\n".format(6 - errors))

        if(gender == 1):
            draw.disp_hang(errors)
        else:
            draw.disp_hang_w(errors)
        player_w = game.initialize_player_w(secret_w, gessed)
        print(player_w)

        gess = " "
        while(gess in gessed):
            gess = security.input_char("Your gess: ")
        gessed.append(gess)
        if(not(gess in secret_w)):
            errors += 1
        player_w = game.initialize_player_w(secret_w, gessed)
        security.clear()

    if(not game.word_diff(secret_w, player_w)):
        print(player_w)
        print("You win !!\nDo you want to play again ? (y/n)")
        play = game.play_again()
    else:
        print("The word was {}".format(secret_w))
        if(gender == 1):
            draw.disp_hang(errors)
        else:
            draw.disp_hang_w(errors)
        print("Sorry... want to try again ? (y/n)")
        play = game.play_again()
