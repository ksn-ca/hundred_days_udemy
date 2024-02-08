import requests
from decouple import config
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.API_KEY = config('SHEETY_APY_KEY')
        self.URL = config('SHEETY_URL')

    def get_header(self):
        return {'Authorization': f'Bearer {self.API_KEY}'}

    def get_sheety_info(self):
        response = requests.get(self.URL, headers={'Authorization': f'Bearer {self.API_KEY}'})
        response.raise_for_status()
        return response.json()['prices']

    def update_sheety_info(self, id, code):
        api = f'{self.URL}/{id}'
        response = requests.put(api, headers=self.get_header(), json={ 'price': {'iataCode': code} })
        response.raise_for_status()
        # print(response.json())


