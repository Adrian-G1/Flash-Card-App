from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------- NEW FLASH CARD --------------------------- #
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def new_card():
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(card_image, image=front_card_img)
    flip_timer = window.after(3000, flip_card, current_card)


# ----------------------------- FLIP CARD ------------------------------ #
def flip_card(card: dict):
    canvas.itemconfig(card_image, image=back_card_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=card["English"], fill="white")


# --------------------------- SAVE PROGRESS ---------------------------- #
def known_word():
    pass


# ------------------------------ UI SETUP ------------------------------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_card_img)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

# # Label
# title_label = Label(text="Title", fg="black", bg="white")
# title_label.config(font=("Ariel", 40, "italic"))
# title_label.place(x=350, y=150)
#
# word_label = Label(text="Word", fg="black", bg="white")
# word_label.config(font=("Ariel", 60, "bold"))
# word_label.place(x=320, y=265)

# Button
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, borderwidth=0, command=new_card)
cross_button.grid(column=0, row=1)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, borderwidth=0, command=new_card)
check_button.grid(column=1, row=1)

new_card()

window.mainloop()
