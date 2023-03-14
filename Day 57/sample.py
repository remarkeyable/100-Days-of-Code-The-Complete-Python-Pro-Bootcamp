import requests



a = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
b= a.json()

for i in b:
    print(i['title'])