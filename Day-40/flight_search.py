import requests

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = "https://api.tequila.kiwi.com/v2/search/"
        self.headers = {
            "apikey": "6doh8g2U9Bu_snzsybRqXaQxptdE4xD0"
        }

    def get_flight_data(self, to):
        parameters = {
            "fly_from": "MAA",
            "fly_to": to,
            "date_from": "18/07/2023",
            "date_to": "18/12/2023",
            "curr": "INR",
            "max_stopovers": 0
        }
        response = requests.get(url=self.url, params=parameters, headers=self.headers).json()
        return response
    def get_flight_data_ws(self, to):
        parameters = {
            "fly_from": "MAA",
            "fly_to": to,
            "date_from": "18/07/2023",
            "date_to": "18/12/2023",
            "curr": "INR",
            "max_stopovers": 1
        }
        response = requests.get(url=self.url, params=parameters, headers=self.headers).json()
        return response
    
    def get_city_code(self, city):
        loc_endpoint = "https://api.tequila.kiwi.com/locations/query"
        city_params = {
            "term" : city
        }
        city_resp = requests.get(url=loc_endpoint, params=city_params, headers=self.headers).json()
        return city_resp["locations"][0]['code']
