import requests
import os
from twilio.rest import Client
from datetime import datetime


# Your Twilio account details
account_sid = "AC70c2d9568e8697cc25467fb084e74034"
auth_token = os.environ.get("TW_AUTH_TOKEN")

# Your OpenWeatherMap API key
api_key = "69f04e4613056b159c2761a9d9e664d2"

# Create a Twilio client object with your account_sid and auth_token
client = Client(account_sid, auth_token)

# Set the API endpoint for OpenWeatherMap and parameters for the request
url = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat" : 13.0632,
    "lon" : 80.2250,
    "appid" : api_key,
}

# Send a GET request to the OpenWeatherMap API with the specified parameters and retrieve the response
response = requests.get(url, params = parameters)
# Initialize a variable to track whether it will rain
will_rain = False

# Extract the weather data for the next 12 hours from the response
start_time = 8
raining_hours = ()
hourly_sliced = response.json()["hourly"][start_time:20]

# Check if it will rain in the next 12 hours
for hour_data in hourly_sliced:
    hour_code = int(hour_data["weather"][0]["id"])
    if hour_code < 700:  # if the weather condition is less than 700, it means it will rain
        will_rain = True
        
        time_str = datetime.strptime(f'{start_time}:00', '%H:%M').strftime('%-I %p')
        raining_hours += (time_str,)
    start_time += 1

total_raining = str(raining_hours).replace("'", "")


# If it will rain, send a message via Twilio to the specified phone number
# if will_rain:
#     message = client.messages.create(
#         body = f"It will rain today at {total_raining}. Take an ☂️🌦️⛈️",
#         from_ = '+14849699513', # Your Twilio phone number
#         to = '+917338961810' # The recipient's phone number
#     )