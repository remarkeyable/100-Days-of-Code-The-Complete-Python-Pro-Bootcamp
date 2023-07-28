from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
import time

LINK = os.environ['LINK']
FILE_PATH = os.environ['FILE_PATH']

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument(rf'--user-data-dir={FILE_PATH}')
chrome_options.add_argument(r"--profile-directory=Profile 10")
chrome_options.add_argument('--start-maximized')
drive = webdriver.Chrome(options=chrome_options)
drive.get(LINK)
time.sleep(2)
