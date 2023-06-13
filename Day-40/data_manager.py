import requests
from flight_search import FlightSearch

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.sheety_data = []
        self.sheety_dict={}
        self.SHEETY_ENDPOINT = "https://api.sheety.co/081557a0ce02affee27d6b05aee415b0/flightDeals/prices"
        self.USER_ENDPOINT = "https://api.sheety.co/081557a0ce02affee27d6b05aee415b0/flightDeals/users"
        TOKEN = "a;wlrkjf3wq[app;'';rkfq[p'akfr[p"
        self.SHEETY_HEADERS = {"Authorization": f"Bearer {TOKEN}"}

    def get_sheet_data(self):
        self.sheet_content = requests.get(url=self.SHEETY_ENDPOINT, headers=self.SHEETY_HEADERS).json()
        for row in self.sheet_content['prices']:
            self.sheety_dict={}
            self.sheety_dict["sheety_price"] = row.get("lowestPrice")
            self.sheety_dict["to_city"] = row.get("city")
            self.sheety_dict["to_city_iata"] = row.get("iataCode")
            self.sheety_data.append(self.sheety_dict)
            # self.sheety_dict[to_city] = sheety_price 
        return self.sheety_data

    def get_cities(self):
        destination_data = self.sheet_content["prices"] 
        return destination_data

    def update_sheety(self):
        for row in self.get_cities():
            new_data = {"price" : {"iataCode" : FlightSearch().get_city_code((row["city"]))}}
    
            response = requests.put(url=f"{self.update_endpoint}/{row['id']}", json=new_data, headers = self.SHEETY_HEADERS)
            
    def get_user_mail(self):
        self.users_mail = requests.get(url=self.USER_ENDPOINT, headers = self.SHEETY_HEADERS).json()
        self.users_list = [user_data.get("email") for user_data in self.users_mail["users"]]
        return self.users_list