from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------- NEW FLASH CARD --------------------------- #
data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict()

# ------------------------------ UI SETUP ------------------------------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
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
cross_button = Button(image=cross_img, borderwidth=0)
cross_button.grid(column=0, row=1)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, borderwidth=0)
check_button.grid(column=1, row=1)

window.mainloop()
