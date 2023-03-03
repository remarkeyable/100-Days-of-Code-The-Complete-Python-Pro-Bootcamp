import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
import os

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
URL = "https://www.amazon.com/dp/B08ML2QXJT/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0",
    "Accept-Language" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}

req = requests.get(URL, headers=head)
html = req.text
soup = BeautifulSoup(html, "lxml")
result = soup.select(".a-span12 .a-offscreen")
product_result = soup.select("#productTitle")
product = [i.getText() for i in product_result]
price = [i.getText() for i in result]

if int(float(price[0].strip('$'))) < 50:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=(
            f"Subject: PRODUCT ON SALE ! ! !\n\n{product[0]} is now{price[0]}. \n\n {URL} ").encode(
            'utf8'))
    print("done")
else:
    pass




