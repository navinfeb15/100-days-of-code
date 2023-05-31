import os
import random
import tkinter as tk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Create the main window
window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# LOADING DATA
french_words = pd.read_csv("Day-31/data/french_words.csv")

# Check if the 'words_to_learn.csv' file exists, otherwise create it with the initial data
if not os.path.isfile("Day-31/data/words_to_learn.csv"):
    french_words.to_csv("Day-31/data/words_to_learn.csv", index=False)

# Read the data from 'words_to_learn.csv' into a dictionary
data = pd.read_csv("Day-31/data/words_to_learn.csv")
data_dict = data.to_dict(orient="records")

# Function to show the answer (English translation) on the flashcard
def show_answer():
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_word["English"])
    canvas.itemconfig(bg_image, image=card_back)

# Function to move to the next flashcard
def next_card():
    global current_word, flip_timer
    current_word = random.choice(data_dict)
    window.after_cancel(flip_timer)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_word["French"])
    canvas.itemconfig(bg_image, image=card_front)
    flip_timer = window.after(3000, show_answer)

# Function to handle the correct answer
def correct_function():
    data_dict.remove(current_word)
    new_data = pd.DataFrame(data_dict)
    new_data.to_csv("Day-31/data/words_to_learn.csv", index=False)
    next_card()

# Create the canvas widget for the flashcard
canvas = tk.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
flip_timer = canvas.after(3000, show_answer)

# Load the card images
card_back = tk.PhotoImage(file="Day-31/images/card_back.png")
wrong_pic = tk.PhotoImage(file="Day-31/images/wrong.png")
right_pic = tk.PhotoImage(file="Day-31/images/right.png")
card_front = tk.PhotoImage(file="Day-31/images/card_front.png")
bg_image = canvas.create_image(400, 268, image=card_front)

# Create the text elements for the flashcard
title_text = canvas.create_text(400, 150, text=" ", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text=" ", font=("Arial", 40, "italic"))

# Create the buttons for wrong and correct answers
wrong_button = tk.Button(image=wrong_pic, highlightthickness=0, command=next_card)
right_button = tk.Button(image=right_pic, highlightthickness=0, command=correct_function)

# Grid layout for the canvas and buttons
canvas.grid(column=0, row=0, columnspan=2, pady=(0, 20))
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

# Start with the first flashcard
next_card()

# Start the tkinter event loop
window.mainloop()
