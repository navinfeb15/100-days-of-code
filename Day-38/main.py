import os
import requests
from datetime import datetime

# Set up API credentials
APP_ID = "f83349cf"
API_KEY = "f176d0773cf10ffee298fe5c8c132fa8"


# Prompt user for input
consumption = input("Tell me which exercise you did?\n")

# Set up endpoint and headers for Nutritionix API request
workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise/"
workout_params = {"query": consumption}
headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}

# Make request to Nutritionix API
workout_resp = requests.post(url=workout_endpoint, headers=headers, json=workout_params).json()

# Get current date and time in desired format for Sheety API
cur_date = datetime.now().strftime("%d/%m/%Y")
cur_time = datetime.now().strftime("%H:00:00")

# Set up endpoint, headers, and payload for Sheety API request
# Token has been removed from code for security reasons
SHEETY_ENDPOINT = "https://api.sheety.co/a0d82131776d41e5ab3537f55dee7f5d/myWorkout/workouts"
TOKEN = "<YOUR_SHEETY_API_TOKEN>"
SHEETY_HEADERS = {"Authorization": f"Bearer {TOKEN}"}
SHEETY_PARAMS = {"workout": {"date": cur_date, "time": cur_time, "exercise": "", "duration": "", "calories": ""}}

# Function to add data to Sheety API
def add_data(exercise, duration, calories):
    SHEETY_PARAMS["workout"]["exercise"] = exercise
    SHEETY_PARAMS["workout"]["duration"] = duration
    SHEETY_PARAMS["workout"]["calories"] = calories
    sheety_resp = requests.post(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS, json=SHEETY_PARAMS)
    sheety_resp.raise_for_status()  # raise an exception if the response returned a non-2xx status code

# Loop through exercises returned by Nutritionix API and add each one to Sheety API
for activity in workout_resp["exercises"]:
    exercise = activity["user_input"]
    duration = activity["duration_min"]
    calories = activity["nf_calories"]
    add_data(exercise, duration, calories)