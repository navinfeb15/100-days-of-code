class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, f_data):
        self.deal_list = []
        self.f_data = f_data

    def format_flight_data(self):
        for deal in self.f_data["data"]:
            deal_dict = {}
            deal_dict["deal_id"] = deal["id"]
            deal_dict["fly_to"] = deal["flyTo"]
            deal_dict["dep_date"] = deal["local_departure"].split("T")[0]
            deal_dict["flight_price"] = deal["price"]
            deal_dict["deal_link"] = deal["deep_link"]
            self.deal_list.append(deal_dict)
            self.deal_list = sorted(self.deal_list, key=lambda x: x['flight_price'])
        return self.deal_list
