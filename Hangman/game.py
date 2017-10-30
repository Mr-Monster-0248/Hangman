import random
import security

#function that return a word randomly choosen in word_list.txt
def choose_word_ia():
    with open("word_list.txt", "r") as word_list:
        words = word_list.read().strip().split("\n")
    return random.choice(words)

def choose_word_player():
    return security.input_word("Enter your word: ")
