from selen import webdriver
from selen.webdriver.chrome.options import Options
from selen.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
import time
#---------------------------
G_DOCS = os.environ['G_DOCS']
FILE_PATH = os.environ['FILE_PATH']
LINK = os.environ['LINK']
#---------------------------
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument(rf'--user-data-dir={FILE_PATH}')
chrome_options.add_argument(r"--profile-directory=Profile 10")
chrome_options.add_argument('--start-maximized')
drive = webdriver.Chrome(options=chrome_options)
drive.get(G_DOCS)
time.sleep(2)
#--------------------------- BEAUTIFUL SOUP ------------
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0",
    "Accept-Language" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}
request = requests.get(LINK ,headers= head)
response = request.text
soup = BeautifulSoup(response, 'html.parser')

data= soup.find_all(name='a', class_='StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0')
data2= soup.find_all(class_='StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0')
#---------------------------
clean = [i.get('href').replace('https://www.zillow.com/', '') for i in data]
links = [f"https://www.zillow.com{i}" for i in clean]
prices = []
locations = []
for i in data2:
    loc = i.find_all('address')
    for j in loc:
        locations.append(j.getText())
    price = i.find_all('span')
    for j in price:
        prices.append(j.getText().split()[0].replace("+", '').replace('/mo', ''))


count = 0
on = True
while on:
    address = drive.find_element(By.XPATH,
                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = drive.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = drive.find_element(By.XPATH,
                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = drive.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    address.send_keys(locations[count])
    price.send_keys(prices[count])
    link.send_keys(links[count])
    submit.click()
    time.sleep(2)
    another = drive.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another.click()
    count +=1
    if count == int(len(links)-1):
        on = False
