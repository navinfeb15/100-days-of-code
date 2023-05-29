from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import json
import os
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generate a random password and copy it to the clipboard."""
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
    """Save the entered website, email, and password to a JSON file."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        user_choice = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?"
        )
        if user_choice:
            new_data = {
                website: {
                    "Email": email,
                    "Password": password
                }
            }
            try:
                with open("Day-29/data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("Day-29/data.json", "a") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)

                with open("Day-29/data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def search_password():
    """Search for a saved password in the JSON file."""
    try:
        website = website_entry.get()
        with open("Day-29/data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No File Found to search...")
    else:
        searched_data = data.get(website)
        messagebox.showinfo(title="Result", message=f"Email: {searched_data['Email']}\nPassword: {searched_data['Password']}")

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
search_button = Button(text="Search", command=search_password)
add_button = Button(text="Add", command=save_data)

website_label.grid(column=0, row=1, sticky=EW)
website_entry.grid(column=1, row=1, columnspan=2, sticky=EW)
email_label.grid(column=0, row=2, sticky=EW)
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
password_label.grid(column=0, row=3, sticky=EW)
password_entry.grid(column=1, row=3, sticky=EW)
search_button.grid(column=2, row=1, sticky=EW)
generate_button.grid(column=2, row=3, sticky=EW)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

canvas.grid(column=1, row=0)

website_entry.focus()
email_entry.insert(0, freq_email)

window.mainloop()
