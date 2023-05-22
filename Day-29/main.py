from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Define lists of letters, numbers, and symbols that can be used to generate passwords
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
        "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    # Generate the password by appending random characters from the lists to a list called 'password'
    password = [choice(letters) for i in range(randint(8, 10))]
    password += [choice(symbols) for i in range(randint(2, 4))]
    password += [choice(numbers) for i in range(randint(2, 4))]

    # Shuffle the characters in the password list and print the resulting password
    shuffle(password)
    generated_password = "".join(password)
    pyperclip.copy(generated_password)

    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    if len(website_entry.get()) < 1 or len(password_entry.get()) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        user_choice = messagebox.askokcancel(
            title=website_entry.get(),
            message=f"These are the details entered:\nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\nIs it ok to save?"
        )
        if user_choice:
            with open("Day-29/data.txt", "a") as file:
                credentials = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n"
                file.write(credentials)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
freq_email = "yourname@gmail.com"

window = Tk()
window.title("PASSWORD GENERATOR")
window.config(padx=30, pady=30)

canvas = Canvas(width=250, height=250, highlightthickness=0)
pic = PhotoImage(file="Day-29\logo.png")
canvas.create_image(125, 125, image=pic)

website_label = Label(text="Website:")
website_entry = Entry()

email_label = Label(text="Email/Username:")
email_entry = Entry()
password_label = Label(text="Password:")
password_entry = Entry()
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", command=save_data)

website_label.grid(column=0, row=1, sticky=EW)
website_entry.grid(column=1, row=1, columnspan=2, sticky=EW)
email_label.grid(column=0, row=2, sticky=EW)
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
password_label.grid(column=0, row=3, sticky=EW)
password_entry.grid(column=1, row=3, sticky=EW)
generate_button.grid(column=2, row=3, sticky=EW)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

canvas.grid(column=1, row=0)

website_entry.focus()
email_entry.insert(0, freq_email)

window.mainloop()