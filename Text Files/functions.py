#Display the number of words and the number of characters in a file
def numberOfWords():
    characters = 0
    number_w = 0
    with open("test.txt", "r") as my_file:
        for word in my_file:
            characters = characters + len(word[:-1]) #to avoid \n character
            number_w += 1
    print("There is {} words and {} characters in the file".format(number_w, characters))
