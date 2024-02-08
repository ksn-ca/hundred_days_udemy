import requests
from datetime import datetime as dt, timedelta
from flight_data import FlightData
from decouple import config


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.URL = "https://api.tequila.kiwi.com/"
        self.get_locations = "locations/query"
        self.search_url = self.URL + 'v2/search'
        self.API_KEY = config('KIWI_API_KEY')
        self.get_locations_url = self.URL + self.get_locations

        days_from = (6 * 30) + 1
        self.currency = 'CAD'
        self.start_date = (dt.today() + timedelta(days=1)).strftime('%d/%m/%Y')
        self.end_date = (dt.today() +
                         timedelta(days=days_from)).strftime('%d/%m/%Y')
        self.departure_airport_code = 'YYZ'
        self.departure_city = 'Toronto'
        self.min_days = 7
        self.max_days = 14
        self.max_stopovers = 0

    def get_iata_code(self, city):
        header = {"apikey": self.API_KEY}
        response = requests.get(
            self.get_locations_url,
            params={
                "term": city,
                "limit": 1
            },
            headers=header,
    )
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]

        return code

    def find_flights(self, price_to, arrival_city_code):
        header = {"apikey": self.API_KEY}
        params = {
            'fly_from': self.departure_airport_code,
            'fly_to': arrival_city_code,
            'curr': self.currency,
            'date_from': self.start_date,
            'date_to': self.end_date,
            'nights_in_dst_from': self.min_days,
            'nights_in_dst_to': self.max_days,
            'max_stopovers': self.max_stopovers,
            'price_to': price_to
        }
        response = requests.get(self.search_url, headers=header, params=params)

        try:
            data = response.json()["data"][0]
        except:
            print(f'No flights found for {arrival_city_code}.')
            return None

        price = data['price']
        departure_date = data["route"][0]["local_departure"].split("T")[0]
        return_date = data["route"][1]["local_departure"].split("T")[0]
        days_abroad = data['nightsInDest']
        return FlightData(self.departure_airport_code,
                                 self.departure_city, data['cityTo'],
                                 data['flyTo'], departure_date, return_date,
                                 days_abroad, price)

