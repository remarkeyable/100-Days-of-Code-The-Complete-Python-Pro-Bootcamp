from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
FILE_PATH = os.environ['FILE_PATH']


class InstaFollower:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option('detach', True)
        self.chrome_options.add_argument(rf'--user-data-dir={FILE_PATH}')
        self.chrome_options.add_argument(r"--profile-directory=Profile 10")
        self.chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def follow(self):
        self.driver.get('https://www.instagram.com/nasa/followers/')
        time.sleep(3)
        self.down = self.driver.find_element(By.CSS_SELECTOR,'._aano ._acan')
        self.down.send_keys(Keys.TAB)
        self.down.send_keys(Keys.END)
        self.down.send_keys(Keys.HOME)
        time.sleep(2)
        self.followers = self.driver.find_elements(By.CSS_SELECTOR, '._aano ._acan')
        time.sleep(3)
        for i in self.followers:
            i.click()