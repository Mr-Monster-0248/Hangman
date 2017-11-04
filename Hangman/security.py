#Function to input safely only one char
#It also check if input is a char and not a number
def input_char(text):
    char = str(input(text))
    char = char[0]
    return char

def input_word(text):
    print("Only your first word will be consider")
    word = str(input(text)).strip().split(" ")
    return word[0]

def input_choice():
    try:
        choice = int(input("Your choice: "))
    except(TypeError, ValueError):
        return 0
    return choice
