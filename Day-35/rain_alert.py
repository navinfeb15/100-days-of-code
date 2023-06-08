import requests
import os
from twilio.rest import Client


# Your Twilio account details
account_sid = "AC70c2d9568e8697cc25467fb084e74034"
auth_token = os.environ.get("TW_AUTH_TOKEN")

# Your OpenWeatherMap API key
api_key = os.environ.get("OWM_API_KEY")

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
hourly_sliced = response.json()["hourly"][0:12]

# Check if it will rain in the next 12 hours
for hour_data in hourly_sliced:
    if int(hour_data["weather"][0]["id"]) < 700: # If the weather condition is less than 700, it means it will rain
        will_rain = True

# If it will rain, send a message via Twilio to the specified phone number
if will_rain:
    message = client.messages.create(
        body = "It's going to rain today. Remember to bring an ☂️",
        from_ = '+14849699513', # Your Twilio phone number
        to = '+917338961810' # The recipient's phone number
    )