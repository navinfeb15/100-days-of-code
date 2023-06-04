import datetime as dt
import smtplib
import time

import requests

# Coordinates of your location
MY_LAT = 13.059309
MY_LONG = 80.231542

def in_place():
    # Get the current position of the International Space Station (ISS)
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_latitude = abs(float(iss_response.json()["iss_position"]["latitude"]))
    iss_longitude = abs(float(iss_response.json()["iss_position"]["longitude"]))

    # Check if the ISS is within 5 degrees of your location
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        return True
    else:
        return False

def in_time():
    # Get sunrise and sunset times for your location
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")
    sunset = response.json()["results"]["sunset"].split("T")[1].split(":")
    cur_time = dt.datetime.now()

    # Check if the current time is within the sunrise and sunset time range
    if cur_time.hour >= int(sunset[0]) and cur_time.minute <= int(sunset[1].split("+")[0]) \
            or cur_time.hour <= int(sunrise[0]) and cur_time.minute >= int(sunrise[1].split("+")[0]):
        return True
    else:
        return False

def send_mail():
    my_email = "navinfeb15@gmail.com"
    password = "your gmail application password"
    to = "navinfeb15@gmail.com"
    message = "Subject:ISS above you\n\nHey! The International Space Station is above you. LOOK UP !"

    # Send the email notification
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to, msg=message)

while True:
    # Check if the ISS is above your location and within the correct time range
    if in_place() and in_time():
        print("Sending mail ...")
        send_mail()
    time.sleep(60)
