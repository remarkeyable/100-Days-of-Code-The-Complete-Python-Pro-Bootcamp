from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(r'--user-data-dir=C:\Users\rsdelmonte_asticom\AppData\Local\Google\Chrome')
#---------------------------------------------------------------------
#added this argument to retrive chrome data *which my linked credentials already login, to skip CAPTCHA
chrome_options.add_argument(r'--profile-directory=Profile 10')
#---------------------------------------------------------------------
chrome_options.add_argument("--start-maximized")
chrome_service = Service(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3422411655&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")


#---------------------------------------------------------------------
#Codes for automated login, commented this out to skip CAPTCHA
# link = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
# link.click()
# user_name = driver.find_element(By.CSS_SELECTOR, "#username")
# user_name.send_keys(EMAIL)
# password = driver.find_element(By.CSS_SELECTOR, "#password")
# password.send_keys(PASSWORD)
# sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
# sign_in.click()
# time.sleep(3)


count = 1
save = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
on = True
while on:
    #located this specific element to scroll down til the end of the page.
    load_data = driver.find_element(By.CSS_SELECTOR, '.disabled')
    load_data.send_keys(Keys.TAB)
    load_data.send_keys(Keys.END)
    time.sleep(2)

    result = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results-list .disabled')
    for i in result:
        time.sleep(1)
        i.click()
        time.sleep(1)
        save.click()
    time.sleep(1)
    pages = driver.find_elements(By.CSS_SELECTOR, ".artdeco-pagination__pages li")
    list = []
    for i in pages:
       page_id = i.get_attribute('id')
       list.append(f'//*[@id="{page_id}"]')
    next_page = driver.find_element(By.XPATH, f'{list[count]}')
    next_page.click()
    count +=1
    if count == 8:
        print(list)
        on = False

