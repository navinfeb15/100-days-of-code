import requests
import datetime


# Define the API endpoint and authentication credentials
url_endpoint = "https://pixe.la/v1/users"
TOKEN = "28wyeq982133rUIRJF2rf"
USERNAME = "navinrajak"
GRAPH_ID = "graph1"

# Get the current date in the format required by the Pixela API
today = datetime.datetime.now().strftime("%Y%m%d")

# Define a second date for testing purposes
second_date = datetime.datetime(year=2023, month=6, day=25).strftime("%Y%m%d")

# Define the parameters for creating a new user account
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create a new user account
response = requests.post(url=url_endpoint, json=params)
print(response.text)

# Define the endpoint for creating a new graph
graph_endpoint = f"{url_endpoint}/{USERNAME}/graphs"

# Define the configuration parameters for the new graph
graph_config = {
    "id": "graph1",
    "name": "Cycling_graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

# Add the new graph to the user's account
headers = {"X-USER-TOKEN": TOKEN.encode("utf-8")}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Define the endpoint for adding a new pixel to the graph
pixel_endpoint = f"{url_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Define the configuration parameters for the new pixel
pixel_config = {
    "date": today,
    "quantity": "500",
}

# Add the new pixel to the graph
# pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(pixel_response.text)

# Define the endpoint for updating an existing pixel
update_endpoint = f"{url_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# Define the configuration parameters for updating the pixel
update_pixel_config = {
    "quantity": "5",
}

# Update the existing pixel
# update_response = requests.put(url=update_endpoint, json=update_pixel_config, headers=headers)
# print(update_response.text)

# Define the endpoint for deleting an existing pixel
delete_endpoint = f"{url_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# Delete the existing pixel
# delete_response = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_response.text)