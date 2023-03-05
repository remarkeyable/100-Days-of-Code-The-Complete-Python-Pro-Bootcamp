from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_service = Service(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service, options = chrome_options)
driver.get("https://www.appbrewery.co/p/newsletter")
result = driver.find_element(By.XPATH, '//*[@id="member_email"]')
result.send_keys("sampleemail@gmail.com")
result.send_keys(Keys.ENTER)