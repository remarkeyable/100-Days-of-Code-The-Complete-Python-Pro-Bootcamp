import requests
from datetime import datetime

USER_NAME = ""
TOKEN = ""
endpoint = "https://pixe.la/v1/users"

parameter = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

g_params = {
    "id": "graph2",
    "name": "Meditation Graph",
    "unit": "min",
    "type": "int",
    "color": "ajisai",
}

header = {
    "X-USER-TOKEN": TOKEN,
}



# graph = f"{endpoint}/{USER_NAME}/graphs"
# g_req = requests.post(url=graph, json= g_params, headers= header)

today = datetime(year=2023, month=2, day= 19)

p_graph = f"{endpoint}/{USER_NAME}/graphs/graph2/{today.strftime('%Y%m%d')}"
request_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "35",
    "color": "ajisai"
}
requests.delete(url=p_graph,headers= header)
