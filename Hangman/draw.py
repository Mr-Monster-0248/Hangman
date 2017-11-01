#First sketch no error
def fig1:
    print("   ------")
    print("   |    |")
    print("        |")
    print("        |")
    print("        |")
    print("        |")
    print("        |")
    print("        |")
    print(" _______|___")

#Sketch 2 1 error
def fig2:
    print("   ------")
    print("   |    |")
    print("  ( )   |")
    print("        |")
    print("        |")
    print("        |")
    print("        |")
    print("        |")
    print(" _______|___")

#Sketch 3 2 errors
def fig3:
    print("   ------")
    print("   |    |")
    print("  ( )   |")
    print("   |    |")
    print("   |    |")
    print("        |")
    print("        |")
    print("        |")
    print(" _______|___")

#Sketch 4 3 errors
def fig4:
    print("   ------")
    print("   |    |")
    print("  ( )   |")
    print(" / |    |")
    print("/  |    |")
    print("        |")
    print("        |")
    print("        |")
    print(" _______|___")

#Sketch 5 4 errors
def fig5:
    print("   ------")
    print("   |    |")
    print("  ( )   |")
    print(" / | \  |")
    print("/  |  \ |")
    print("        |")
    print("        |")
    print("        |")
    print(" _______|___")

#Sketch 6 5 errors
def fig6:
    print("   ------")
    print("   |    |")
    print("  ( )   |")
    print(" / | \  |")
    print("/  |  \ |")
    print("  /     |")
    print(" /      |")
    print("        |")
    print(" _______|___")

#Sketch 7 6 errors end of game
def fig7:
    print("   ------")
    print("   |    |")
    print("  ( )   |")
    print(" / | \  |")
    print("/  |  \ |")
    print("  / \   |")
    print(" /   \  |")
    print("        |")
    print(" _______|___")

def disp_hang(errors):
    if(errors == 0):
        fig1()
    elif(errors == 1):
        fig2()
    elif(errors == 3):
        fig3()
    elif(errors == 3):
        fig4()
    elif(errors == 4):
        fig5()
    elif(errors == 5):
        fig6()
    elif(errors == 6):
        fig7()
