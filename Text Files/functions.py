#Display the number of words and the number of characters in a file
def numberOfWords(wordList):

    """Display the number of words and the number of characters in a file"""

    characters = 0
    number_w = len(wordList)
    for word in wordList:
        if(len(word) == 0):
            number_w = number_w - 1
        else:
            characters = characters + len(word)
    print("There is {} word and {} characters in the file".format(number_w, characters))
