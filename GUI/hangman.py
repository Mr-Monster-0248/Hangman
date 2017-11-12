from tkinter import *

#window creation
my_window = Tk()
my_window.title("Hangman")

#Adding the bg
picture = PhotoImage(file = "./img/sky_bg.png")
Cane = Canvas(my_window, width = picture.width(), height = picture.height())
Cane.create_image(0, 0, anchor=NW, image = picture)
Cane.pack()

#Create the word zone
word_zone = Frame(my_window, width = picture.width(), height = 30, relief = FLAT, bg = "white")
word_zone.pack()

#Print word
word = Label(word_zone, text = "TEST", font = ("Helvetica", 30))
word.pack()

my_window.mainloop()
