from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
FILE_PATH = os.environ['FILE_PATH']


class InternetSpeedTwitterBot:
    def __init__(self):
        self.speed = 0
        self.chrome_options =  Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument(rf'--user-data-dir={FILE_PATH}')
        self.chrome_options.add_argument(r'--profile-directory=Profile 10')
        self.chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options= self.chrome_options)


    def get_internet_speed(self):
        self.driver.get("https://fast.com")
        time.sleep(30)
        self.result = self.driver.find_element(By.XPATH, '//*[@id="speed-value"]')
        self.speed = self.result.text

    def tweet_at_provider(self):
        self.driver.switch_to.new_window('tab')
        self.driver.get("https://twitter.com/home")
        time.sleep(2)
        self.result = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        self.result.click()
        time.sleep(5)
        self.write_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span/br')
        self.write_tweet.send_keys(f"My internet speed is {self.speed} Mbps, I'm paying for 100 Mbps lols. ")
        self.send_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        self.send_tweet.click()



