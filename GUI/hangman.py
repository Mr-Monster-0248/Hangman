from tkinter import *

#window creation
my_window = Tk()
my_window.title("Hangman")

#Adding the bg
picture = PhotoImage(file = "./img/sky_bg.png")
principal_canevas = Canvas(my_window, width = picture.width(), height = picture.height())
principal_canevas.create_image(0, 0, anchor=NW, image = picture)

#text
word = input(">>> ")
player_w = principal_canevas.create_text(640/2, 400, anchor=CENTER, text = word, font = ("DejaVu", 40), width = 640, justify = CENTER)
principal_canevas.pack()

bite = input("test: ")
principal_canevas.delete(player_w)
player_w = principal_canevas.create_text(640/2, 400, anchor=CENTER, text = bite, font = ("DejaVu", 40), width = 640, justify = CENTER)
principal_canevas.pack()

my_window.mainloop()
