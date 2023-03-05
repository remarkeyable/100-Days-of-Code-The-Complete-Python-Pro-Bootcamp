from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver_service = Service(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

driver.get("https://www.python.org")
result = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
result2= driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events= [i.text for i in result2]
date_time= [i.get_attribute("datetime").split("T")[0] for i in result]
dic = {key1:{"Name":j, "Date": i} for i,j,key1 in zip(date_time,events,range(len(events)))}
print(dic)



