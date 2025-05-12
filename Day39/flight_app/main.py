#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint

data_manger = DataManager()
sheet_data = data_manger.get_destination_data()
pprint(sheet_data)