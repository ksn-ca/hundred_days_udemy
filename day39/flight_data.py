class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, departure_airport_code, departure_city, arrival_city,
                 arrival_airport_code, departure_date, return_date,
                 days_abroad, price):
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.arrival_airport_code = arrival_airport_code
        self.departure_date = departure_date
        self.return_date = return_date
        self.days_abroad = days_abroad
        self.price = price
