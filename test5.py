from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pandas
import numpy
import requests
from requests import get
from bs4 import BeautifulSoup
from lxml import etree
import re
import urllib.request


beers = []

CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe"
browser = webdriver.Chrome(CHROMEDRIVER_PATH)
browser.get("https://www.beermenus.com/places/15142-astoria-bier-and-cheese-ditmars")
time.sleep(5)
response = browser.page_source
soup1 = BeautifulSoup(response, "html.parser")
beer_div1 = soup1.find_all('ul', id = 'on_tap')
for d in beer_div1:
    divs = d.find_all('li', class_ = 'pure-list-item')
    for container in divs:
        name = container.h3.a.text
        beers.append(name)
        
print(beers)
browser.quit() 