from functions import *

my_file = open("test.txt", "r")
wordList = my_file.read().split("\n")
my_file.close()

print(wordList)
numberOfWords()
