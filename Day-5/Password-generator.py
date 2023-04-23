import random

# Define lists of letters, numbers, and symbols that can be used to generate passwords
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome the user to the password generator and ask for their desired password parameters
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Generate the password by appending random characters from the lists to a list called 'password'
password = []
for i in range(nr_letters):
    password.append(random.choice(letters))
for i in range(nr_symbols):
    password.append(random.choice(symbols))
for i in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle the characters in the password list and print the resulting password
random.shuffle(password)
print("".join(password))
