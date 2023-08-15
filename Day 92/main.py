from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import requests
import csv
import time

from selenium.webdriver.common.by import By

LINK = os.environ['LINK']

service = Service(r"C:\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get(LINK)

#
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0",
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", }

request = requests.get(LINK, headers=head)
# response = request.text
# soup = BeautifulSoup(response, 'html.parser')
# title = soup.find_all("h2", class_="bc-heading bc-color-base bc-text-bold")
# prices = soup.find_all(class_="bc-text bc-size-base bc-color-base")
# links = soup.find_all(class_="bc-link bc-color-link")
book_title = []
book_price = []
book_link = []
books = []
count = 0
the_books = "com_sci_books.csv"

num = 0
the_limit = None
number_of_pages = None


# def limit():
#     global the_limit
#     start = driver.find_element(By.XPATH, '//*[@id="top-1"]/div/div/div/header/div[1]/span/nav/span/ul/li/a')
#     start.send_keys(Keys.TAB)
#     start.send_keys(Keys.END)
#     lim = driver.find_element(By.XPATH, '//*[@id="pagination-a11y-skiplink-target"]/div/div[2]/div/span/ul/li[5]/a')
#
#     the_limit = int(lim.text)


#
def pressed():
    global num, the_limit, count, number_of_pages, books

    try:
        start = driver.find_element(By.XPATH, '//*[@id="top-1"]/div/div/div/header/div[1]/span/nav/span/ul/li/a')
        start.send_keys(Keys.TAB)
        start.send_keys(Keys.END)
        the_tittle = driver.find_elements(By.ID, 'center-3')
        for i in the_tittle:
            bc_item = i.find_elements(By.CLASS_NAME, 'bc-list-item')
            bc_link = i.find_elements(By.CLASS_NAME, 'bc-link')
            bc_price = i.find_elements(By.CLASS_NAME, 'bc-text')
            for j in bc_item:
                title = j.get_attribute('aria-label')
                if title == None:
                    pass
                else:
                    book_title.append(title)

            for k in bc_link:
                link = k.get_attribute('href')
                book_link.append(link)

            for l in bc_price:
                price = l.text
                if "$" in price and "Regular" not in price:
                    book_price.append(price)

            for m in range(len(book_title)):
                bk = {'Book': book_title[m], 'Price': book_price[m], 'Link': book_link[m]}
                books.append(bk)

        if the_limit == None:
            lim = driver.find_element(By.XPATH,
                                      '//*[@id="pagination-a11y-skiplink-target"]/div/div[2]/div/span/ul/li[5]/a')
            the_limit = int(lim.text) - 3
            number_of_pages = int(lim.text)

        page = driver.find_element(By.XPATH,
                                   f'//*[@id="pagination-a11y-skiplink-target"]/div/div[2]/div/span/ul/li[{the_limit}]/a')
        page.click()
        num += 1
        count += 1
        if the_limit != number_of_pages:
            the_limit += 1
    except:
        num += 1


def export_csv():
    with open(the_books, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Book', 'Price', 'Link'])
        for book in books:
            writer.writerow([book['Book'], book['Price'], book['Link']])


on = True

while on:
    pressed()
    print(num, the_limit)
    if num == the_limit:
        on = False
        export_csv()
