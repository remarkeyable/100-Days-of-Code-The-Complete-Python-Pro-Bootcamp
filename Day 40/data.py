import os
import requests

KEY= os.environ['KEY']
END_POINT = "https://api.tequila.kiwi.com/"

class Data:
    def __init__(self):
        self.prices = {}
        self.header = {
            "apikey": KEY,
        }

    def iata(self, location):
        iata = {
            "term": location,
        }
        result = requests.get(f"{END_POINT}locations/query", params=iata, headers=self.header)
        self.loc = result.json()['locations'][0]['id']
        return self.loc

    def search(self, fly_from, fly_to, date_from, date_to, nights_dst):
        flight = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": nights_dst,
            "flight_type": "round",
            "one_for_city": 1,
                }
        request = requests.get(f"{END_POINT}v2/search", headers= self.header, params=flight)
        result = request.json()['data'][0]
        print(result['price'])






