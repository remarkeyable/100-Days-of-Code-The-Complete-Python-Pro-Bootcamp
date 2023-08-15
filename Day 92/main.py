from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import csv

from selenium.webdriver.common.by import By

service = Service(r"C:\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.audible.com/search")
topic = None
the_books = None
number_of_pages = None
book_title = []
book_price = []
book_link = []
books = []
num = 0
the_limit = 2
the_page = 3


def search():
    global topic, the_books
    keyword = input("Enter topic to find: ").title()
    look = driver.find_element(By.XPATH, '//*[@id="header-search"]')
    look.send_keys(keyword)
    look.send_keys(Keys.ENTER)
    topic = keyword
    the_books = f"{topic}.csv"
    print(f"{topic} books are now processing....")


def pressed():
    global num, the_limit, count, number_of_pages, books, the_page
    start = driver.find_element(By.XPATH, '//*[@id="top-1"]/div/div/div/header/div[1]/span/nav/span/ul/li/a')
    the_tittle = driver.find_elements(By.ID, 'center-3')
    if the_limit - 1 != num:
        start.send_keys(Keys.TAB)
        start.send_keys(Keys.END)

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

            if "$" in price and "Regular" not in price or "Free with Plus trial" in price:
                book_price.append(price)

        for m in range(len(book_title)):
            bk = {'Book': book_title[m], 'Price': book_price[m], 'Link': book_link[m]}
            books.append(bk)

    if the_limit == 2:
        lim = driver.find_element(By.XPATH, '//*[@id="pagination-a11y-skiplink-target"]/div/div[2]/div/span/ul/li[5]/a')
        the_limit = int(lim.text) - 3
        number_of_pages = int(lim.text)

    if the_limit - 1 != num:
        page = driver.find_element(By.XPATH,
                                   f'//*[@id="pagination-a11y-skiplink-target"]/div/div[2]/div/span/ul/li[{the_page}]/a')
        page.click()
        num += 1
        if the_page != 6:
            the_page += 1
        if the_limit != number_of_pages:
            the_limit += 1


def export_csv():
    with open(the_books, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Book', 'Price', 'Link'])
        for book in books:
            writer.writerow([book['Book'], book['Price'], book['Link']])


search()
on = True
while on:
    try:
        pressed()
    except:
        print(f'No results for "{topic}" in All Categories')
        on = False
    if num == the_limit - 1:
        pressed()
        export_csv()
        print("Done! File Saved")
        on = False
