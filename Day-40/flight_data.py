class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self):
        self.deal_list = []

    def format_flight_data(self, f_data):
        # Method to format flight data and structure it into a list of dictionaries
        self.deal_list.clear()
        self.f_data = f_data
        for deal in self.f_data["data"]:
            deal_dict = {}
            deal_dict["deal_id"] = deal["id"]
            deal_dict["fly_to"] = deal["flyTo"]
            deal_dict["dep_date"] = deal["local_departure"].split("T")[0]
            deal_dict["flight_price"] = deal["price"]
            deal_dict["deal_link"] = deal["deep_link"]
            if len(deal["route"]) > 1:
                deal_dict["has_stopover"] = True
                deal_dict["stopover_city"] = deal["route"][1].get("cityFrom")
            self.deal_list.append(deal_dict)
            self.deal_list = sorted(self.deal_list, key=lambda x: x['flight_price'])
        return self.deal_list

    def update_destination_codes(self):
        # Method to update destination codes in the Google Sheet
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)