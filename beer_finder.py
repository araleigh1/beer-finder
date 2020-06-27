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


CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe"

zip_code = input("PLEASE INPUT A ZIP CODE (e.g. 06510): ")


CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get("https://www.beermenus.com/places")
searchbox_xpath = '//*[@id="location_address"]'
searchbox = driver.find_element_by_xpath(searchbox_xpath)
search_term = zip_code
searchbox.click()
searchbox.send_keys(Keys.CONTROL,"a", Keys.DELETE)
searchbox.send_keys(search_term)
time.sleep(1)
searchbox.send_keys(Keys.RETURN)
time.sleep(2)
searchbox.send_keys(Keys.RETURN)
time.sleep(10)
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")

place = []

beer_div = soup.find_all('div', class_= 'pure-u-1')
for container in beer_div:
    name = container.h3.a.text
    place.append(name)

print(place)


#final_result = []
#names = ['name1', 'name2', 'name3']
#for name in names:
#    final_result.append(get_results(name))

#print(final_result) 

