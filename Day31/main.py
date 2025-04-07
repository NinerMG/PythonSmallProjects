# Capstone Project - Flash Card Program

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])

def flip_card():
    canvas.itemconfig(card_title, text="Polish")
    canvas.itemconfig(card_word, text=current_card["Polish"])

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,background=BACKGROUND_COLOR)

window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_button_image = PhotoImage(file="images/right.png")
wrong_button_image = PhotoImage(file="images/wrong.png")


# front card and text
canvas.create_image(400,263, image=card_front)
card_title = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

# adding button
right_button = Button(image=right_button_image, highlightthickness=0, command=next_card)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)


next_card()



window.mainloop()
