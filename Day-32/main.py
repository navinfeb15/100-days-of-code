import smtplib
import os
import random
import datetime as dt
import pandas as pd

# Step 1: Update the birthdays.csv file
file = pd.read_csv("birthdays.csv")

# Step 2: Check if today matches a birthday in the birthdays.csv
IS_BIRTHDAY = False
now = dt.datetime.now()
cur_day = (now.month, now.day)

# Create a dictionary of birthday date tuples to birthday person rows
birthdays_tuple = {(row.month, row.day): row for index, row in file.iterrows()}

# Check if today's date is in the dictionary of birthdays
if cur_day in birthdays_tuple:
    birthday_person = birthdays_tuple[cur_day]
    IS_BIRTHDAY = True

    # Choose a random letter template and replace the name with the birthday person's name
    letter = random.choice(os.listdir("letter_templates"))
    with open(letter) as file:
        template = file.read()
    message = template.replace("[NAME]", birthday_person["name"])

    # Send the birthday email using Gmail SMTP
    my_email = "navinfeb15@gmail.com"
    password = "your gmail application password"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"], msg=message)