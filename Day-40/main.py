#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from add_user import addUser


data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

# new_user = addUser()
sheety_list = data_manager.get_sheet_data()

for record in sheety_list:
    sheety_price = record["sheety_price"]
    
    try:
        flight_datas = flight_search.get_flight_data(record["to_city_iata"])
        deal_list = flight_data.format_flight_data(flight_datas)
        lowest_price = deal_list[0]["flight_price"]
    except IndexError:
        flight_datas = flight_search.get_flight_data_ws(record["to_city_iata"])
        deal_list = flight_data.format_flight_data(flight_datas)
        lowest_price = deal_list[0]["flight_price"]
    
    if lowest_price >= sheety_price:
        notification_manager = NotificationManager(deal_list, record)
        # notification_manager.send_alert()
        notification_manager.send_mail()