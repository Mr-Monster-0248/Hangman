#Display the words of the list where the first and the last characters have been removed
def dispWord(listOfWords):

    """Display the words of the list where the first and the last characters have been removed"""

    for word in listOfWords:
        print(word[1:-1])

#Find the longest word of the list
def longest(listOfWords):

    """Find the longest word of the list"""

    larger = ""
    maxLen = 0
    for word in listOfWords:
        if(len(word) > maxlen):
            maxLen = len(word)
            larger = word

    return larger

#Creat a list of integers representing the lenght of the corresponding word in the list
def listLenght(listOfWords):

    """Creat a list of integers representing the lenght of the corresponding word in the list"""

    lenghtOfWords = []
    for word in listOfWords:
        lenghtOfWords.append(len(word))

    return lenghtOfWords

#Display the number of item in the list followed by elements of the list
def dispItems(listOfWords):

    """Display the number of item in the list followed by elements of the list"""

    print("There is {} item in the list, they are:".format(len(listOfWords)))
    for word in listOfWords:
        print("{word}, ".format(word = word), end="")

#Removes all the occurrence of a given word
def removeAll(listOfWords, toRemove):

    """Removes all the occurrence of a given word"""

    if((toRemove in listOfWords) == False):
        print("{toRemove} isn't in the list".format(toRemove = toRemove))
    while toRemove in listOfWords:
        listOfWords.remove(toRemove)

#Replace a word $w_1$ by a word $w_2$
def replace(listOfWords, w_1, w_2):

    """Replace a word $w_1$ by a word $w_2$"""

    if(not(w_1 in listOfWords)):
        print("{word} isn't in the list".format(word = w_1))
    else:
        listOfWords[listOfWords.index(w_1)] = w_2

#Reads a word from the user and display the number of occurrences and their positions
def occurrences(listOfWords, toFind):

    """Reads a word from the user and display the number of occurrences and their positions"""

    occu = 0
    index = []
    if(not(toFind in listOfWords)):
        print("{word} isn't in the list".format(word = toFind))
    else:
        for i in range(len(listOfWords)):
            if(listOfWords[i] == toFind):
                occu += 1
                index.append(str(i))
        print("{word} found at index {index}".format(word = toFind, index = ", ".join(index)))
