import os
import requests
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth

#credentials & endpoints
KEY= os.environ['KEY']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
SHEET_ENDP = "https://api.sheety.co/6c802849bcdd46d608761e2fb8aa6376/flightDeals/prices"
END_POINT = "https://api.tequila.kiwi.com/"
BASIC = HTTPBasicAuth(username= USER, password=PASSWORD)

class Data:
    def __init__(self):
        self.location = {}
        self.prices = {}
        self.header = {
            "apikey": KEY,
        }
        
    #will get data on google sheet via sheety api
    def iata(self):
        data = requests.get(SHEET_ENDP, auth=BASIC)
        print(data)
        self.location = data.json()['prices']

    #will update rows on googlesheet specifically the AITA    
    def update(self):
        for i in self.location:
            iata = {
                "term": i['city']
            }
            #will get data on tequila api and pass to google sheet
            result = requests.get(f"{END_POINT}locations/query", params=iata, headers=self.header)
            parameter = {
                "price": {
                    "iata": result.json()['locations'][0]['id']
                }
            }
            requests.put(f"{SHEET_ENDP}/{i['id']}", auth=BASIC, json=parameter)

    def search(self, cur_loc):
        for j in self.location:
            today_plus = datetime.now() + timedelta(days=30)
            flight = {
                "fly_from": f"{cur_loc}",
                "fly_to": f"{j['iata']}",
                "date_from": datetime.now().strftime("%d/%m/%Y"),
                "date_to": today_plus.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                }
            request = requests.get(f"{END_POINT}v2/search", headers= self.header, params=flight)
            result = request.json()['data'][0]
            parameter = {
                "price": {
                    "seen": f"{result['price']}"
                }
            }
            requests.put(f"{SHEET_ENDP}/{j['id']}", auth=BASIC, json=parameter)




