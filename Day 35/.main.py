API_KEY = ""
MY_LAT = 14.59
MY_LONG = 120.98
account_sid = ""
auth_token = ""
import requests
from twilio.rest import Client
import os

parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
}

client = Client(account_sid, auth_token)
request = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameter)
request.raise_for_status()
result =  request.json()['hourly']
list = []
will_rain = []

for condition in range(0,11):
    weather_cond = result[condition]['weather'][0]['id']
    list.append(weather_cond)
    if weather_cond >= 500 and weather_cond <= 531:
        will_rain.append("rain")

if "rain" in will_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️.",
        from_="+12184135231",
        to="+639568767389"
    )
    print(message.sid)
else:
    message = client.messages.create(
        body="It's a sunny 🌞 day . Don't forget to apply your sunscreen ✨~",
        from_="+12184135231",
        to=""
    )
    print(message.sid)





