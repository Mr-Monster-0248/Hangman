#Display the number of words and the number of characters in a file
def numberOfWords():
    """Display the number of words and the number of characters in a file"""
    characters = 0
    number_w = 0
    with open("test.txt", "r") as my_file:
        for word in my_file:
            characters = characters + len(word[:-1]) #to avoid \n character
            number_w += 1
    print("There is {} words and {} characters in the file".format(number_w, characters))

#This function will be used in the next one
def occurences(my_list, toFind):
    occu = 0
    for word in my_list:
        if(word == toFind):
            occu += 1
    return occu


#Display all the words in the alphabetical order,
#each followed by its number of occurences in the file
def display_word_and_occurrences():
    """
        Display all the words in the alphabetical order,
        each followed by its number of occurences in the file
    """
    with open("test.txt", "r") as my_file:
        wordList = my_file.read().strip().split("\n")

    wordList.sort()
    for word in wordList:
        print("{word} : {occu}".format(word = word, occu = occurences(wordList, word)))
