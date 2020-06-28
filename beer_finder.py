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

CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe"

zip_code = input("PLEASE INPUT A ZIP CODE (e.g. 06510): ")

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
time.sleep(5)
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
driver.quit()
url = []

beer_div = soup.find_all('div', class_= 'pure-u-1')
for div in beer_div:
    links = div.find_all('a')
    for sites in links:
        url.append(sites['href'])

home = "https://www.beermenus.com"

full_url = [home + x for x in url]

print(full_url)
print(len(full_url))

beers = []

browser = webdriver.Chrome(CHROMEDRIVER_PATH)
for u in full_url:
    browser.get(u)
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


#for u in full_url:
 #   driver.get(u)
  #  time.sleep(10)
   # response = driver.page_source
    #soup1 = BeautifulSoup(response.content, "html.parser")
    #beer_div1 = soup1.find_all('div', id = 'menu')
    #for div in beer_div1:
    #    links1 = div.find_all('a')
     #   beers.append(links1)




#for u in full_url:
 #   response = requests.get(u)
  #  soup1 = BeautifulSoup(response.content, "html.parser")
   # beer_div1 = soup1.find_all('div', class_ = 'pure-g')
    #for div in beer_div1:
     #   links1 = div.find_all('a')
      #  beers.append(links1)
