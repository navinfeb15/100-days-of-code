import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.sheety_data = []
        self.sheety_dict={}
        self.SHEETY_ENDPOINT = "https://api.sheety.co/a0d82131776d41e5ab3537f55dee7f5d/flightDeals/prices"
        TOKEN = "a;wlrkjf3wq[app;'';rkfq[p'akfr[p"
        self.SHEETY_HEADERS = {"Authorization": f"Bearer {TOKEN}"}

    def get_sheet_data(self):
        sheet_content = requests.get(url=self.SHEETY_ENDPOINT, headers=self.SHEETY_HEADERS).json()

        for row in sheet_content['prices']:
            self.sheety_dict={}
            self.sheety_dict["sheety_price"] = row.get("lowestPrice")
            self.sheety_dict["to_city"] = row.get("city")
            self.sheety_dict["to_city_iata"] = row.get("iataCode")
            self.sheety_data.append(self.sheety_dict)
            # self.sheety_dict[to_city] = sheety_price 
        return self.sheety_data