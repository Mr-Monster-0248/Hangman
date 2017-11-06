#Function to input safely only one char
#It also check if input is a char and not a number
def input_char(text):
    char = "1"
    while(not char.isalpha()):
        char = str(input(text))
        char = char[0]
    return char.upper()

def input_word(text):
    print("Only your first word will be consider")
    word = str(input(text)).strip().split(" ")
    return word[0].upper()

def input_choice():
    try:
        choice = int(input("Your choice: "))
    except(TypeError, ValueError):
        return 0
    return choice
