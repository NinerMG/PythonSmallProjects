# Capstone Project - Flash Card Program

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    #data = pandas.read_csv("data/french_words.csv")
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data =  pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Polish", fill="white")
    canvas.itemconfig(card_word, text=current_card["Polish"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    to_learn.remove(current_card)
    # print(len(to_learn))

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,background=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_button_image = PhotoImage(file="images/right.png")
wrong_button_image = PhotoImage(file="images/wrong.png")


# front card and text
card_background = canvas.create_image(400,263, image=card_front)
card_title = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

# adding button
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)


next_card()



window.mainloop()
