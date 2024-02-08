#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
sheet_data = data_manager.get_sheety_info()

flight_search = FlightSearch()


for row in sheet_data:
    if row['iataCode'] == '': 
        row['iataCode'] = flight_search.get_iata_code(row['city'])
        data_manager.update_sheety_info(row['id'], row['iataCode'])

for row in sheet_data:

    flight = flight_search.find_flights(
        row['lowestPrice'],
        row['iataCode']
    )
    if flight != None:
        print(f"""Arrival city: {flight.arrival_city}
        Departure date: {flight.departure_date}
        Return date: {flight.return_date}
        Price (CAD): {flight.price}
        """)
