import smtplib
from datetime import datetime
import requests

LAT = 12.8797
LONG = 121.7740


def is_iss_here():
    iss = requests.get("http://api.open-notify.org/iss-now.json")
    iss.raise_for_status()
    iss_data = iss.json()
    iss_lat = float(iss_data['iss_position']['latitude'])
    iss_long = float(iss_data['iss_position']['longitude'])
    if iss_lat <= LAT+5 <= LAT-5 and iss_long <= LONG+5  <= LONG-5:
        return True

def is_night():
    parameter = {
        "formatted": 0,
    }

    request = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    request.raise_for_status()
    data = request.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now()
    now = time_now.hour

    if now >= sunset or now <= sunrise:
        return True
      
if is_iss_here() and is_night():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user="", password="")
        connection.sendmail(from_addr="", to_addrs="", msg="Look up")
