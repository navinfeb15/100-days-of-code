import datetime as dt
import random
import smtplib

my_email = "your gmail application password"
password = "jjvstrmusjmxjttv"
now = dt.datetime.now()

def send_mail(to_address, message):

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_address, msg=message)
        connection.close()





def monday_motivation():

    weekday = now.weekday()

    with open("Day-32/quotes.txt", "r") as file:
        quotes = file.readlines()

    quote = random.choice(quotes)

    message = f"Subject:Test email usingpython SMTPLIB\n\n{quote}"
    send_mail(my_email, message=message)


monday_motivation()
