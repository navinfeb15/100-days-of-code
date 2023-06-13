import requests

api_key = 'YOUR_API_KEY'
url = 'https://tequila-api.kiwi.com/v2/search'

headers = {
    'apikey': "6doh8g2U9Bu_snzsybRqXaQxptdE4xD0"
}

params = {
    'fly_from': 'MAA',    # origin airport code
    'fly_to': 'BER',      # destination airport code
    'date_from': '01/07/2023',  # departure date
    'date_to': '15/12/2023',
    'curr': 'INR',        # currency
    'max_stopovers': 0         # number of adults
}

response = requests.get(url, headers=headers, params=params)
print(response.json())