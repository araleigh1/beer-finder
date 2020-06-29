from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import numpy
import requests
from requests import get
from bs4 import BeautifulSoup
from lxml import etree
import re
import pandas as pd
from app import APP_ENV




CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe"
chrome_options = Options()

chrome_options.add_argument("--headless")
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get("https://www.beeradvocate.com/beer/top-new/")
time.sleep(5)
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
driver.quit()

table = soup.find('table', {'class': 'details'})


beer_div = soup.find_all('div', class_= 'pure-u-1')
for div in beer_div:
    links = div.find_all('a')
    for sites in links:
        url.append(sites['href'])

