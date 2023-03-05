from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_argument("--start-maximized")
chrome_service = Service(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker")
time.sleep(5)
language_select = driver.find_element(By.CSS_SELECTOR, "#promptContentChangeLanguage #langSelect-EN")
language_select.click()
time.sleep(5)
cookie = driver.find_element(By.ID, "bigCookie")
start_time = time.time()
increment = 5
while True:
    if time.time() > increment + start_time:
        try:
            upgrades = driver.find_elements(By.CSS_SELECTOR,"#upgrades .enabled")
            for item in upgrades[::-1]:
                item.click()
        except:
            pass

        try:
            products = driver.find_elements(By.CSS_SELECTOR,".product.enabled")
            for item in products[::-1]:
                item.click()
        except:
            print("Not enough cookies")

        start_time = time.time()
        increment += 5
    cookie.click()
