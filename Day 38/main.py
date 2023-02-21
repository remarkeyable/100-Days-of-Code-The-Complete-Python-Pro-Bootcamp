import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

#credentials & endpoints
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
USER = os.environ["USER"]
PASSWORD = os.environ["PASSWORD"]
SHEET_ENDP = "https://api.sheety.co/6c802849bcdd46d608761e2fb8aa6376/Flight Deals/workouts"
basic = HTTPBasicAuth(username=USER ,password= PASSWORD)
header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

#exer value will be pass to ex_params dictionary, query key
excer = input("Tell me which exercise you did: ")
ex_params = {
    "query": excer,
    "gender":"female",
    "weight_kg": "43",
    "height_cm": "168",
    "age": "22",
}

#will get calorie data from nutrix api
request = requests.post(END_POINT, json=ex_params, headers= header)

data = request.json()
today = datetime.now()
time = today.time()
date = today.strftime("%d/%m/%Y")
activity = data['exercises'][0]['name']
duration = data['exercises'][0]['duration_min']
calories = data['exercises'][0]['nf_calories']

#will post details on gsheet using sheety api
sheet_params = {
    "workout": {
        "date" : date,
        "time" : time.strftime("%X"),
        "exercise": activity.title(),
        "duration": duration,
        "calories": calories,
    }
}

sheet = requests.post(SHEET_ENDP, json=sheet_params, auth=basic)
