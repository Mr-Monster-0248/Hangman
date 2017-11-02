import random
import security

#function that return a word randomly choosen in word_list.txt
def choose_word_ia():
    with open("word_list.txt", "r") as word_list:
        words = word_list.read().strip().split("\n")
    return random.choice(words)

def choose_word_player():
    return security.input_word("Enter your word: ")

def initialize_player_w(secret_w, gessed):
    toDisp = ["_"] * len(secret_w)
    for letter in gessed:
        for i in range(len(secret_w)):
            if(secret_w[i] == letter):
                toDisp[i] = letter
    return " ".join(toDisp)
