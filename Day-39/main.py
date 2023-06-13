# #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# from data_manager import DataManager
# from flight_data import FlightData
# from flight_search import FlightSearch
# from notification_manager import NotificationManager


# data_manager = DataManager()
# flight_search =  FlightSearch()


# sheety_list = data_manager.get_sheet_data()
# for record in sheety_list:
#     # for city in record:
#     sheety_price = record["sheety_price"]
#     flight_datas = flight_search.get_flight_data(record["to_city_iata"])
#     deal_list = FlightData(flight_datas).format_flight_data()
#     lowest_price = deal_list[0]["flight_price"]
    
#     if lowest_price < sheety_price:
#         notification_manager =  NotificationManager(deal_list, record)
#         notification_manager.send_alert()
#     print(record["to_city"]," : ",lowest_price)


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

data_manager.update_sheety()
# flight_data.update_destination_codes()
sheety_list = data_manager.get_sheet_data()
for record in sheety_list:
    sheety_price = record["sheety_price"]
    flight_datas = flight_search.get_flight_data(record["to_city_iata"])
    deal_list = flight_data.format_flight_data(flight_datas)
    lowest_price = deal_list[0]["flight_price"]
    
    if lowest_price < sheety_price:
        notification_manager = NotificationManager(deal_list, record)
        notification_manager.send_alert()