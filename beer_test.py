import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from pprint import pprint
import re
import pandas as pd
from dotenv import load_dotenv
from flask import Flask, request, render_template, session, redirect

load_dotenv()

zip_code = input("PLEASE INPUT A ZIP CODE (e.g. 06510): ")

CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe"
chrome_options = Options()
APP_ENV = "development"


chrome_options.add_argument("--headless")
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

#print(full_url)
#print(len(full_url))

beers = []
beer_sites = []
browser = webdriver.Chrome(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()


for u in full_url[:1]:
    browser.get(u)
    time.sleep(3)
    options.add_argument('--headless')
    response = browser.page_source
    soup1 = BeautifulSoup(response, "html.parser") 
    beer_div1 = soup1.find_all('ul', id = 'on_tap')
    #beer_div2 = soup1.find_all('ul', id = 'cans')
    #beer_div3 = soup1.find_all('ul', id = 'bottles')
    for d in beer_div1:
        divs1 = d.find_all('li', class_ = 'pure-list-item')
        for container in divs1:
            name = container.h3.a.text
            beers.append(name)
    for b in beer_div1:
        divs2 = b.find_all('li', class_ = 'pure-list-item')
        for container1 in divs2:
            links1 = container1.find_all('a')
            for sites1 in links1:
                beer_sites.append(sites1['href'])
    browser.quit()


beer_url = [home + x for x in beer_sites]
#print(beers)
#print(beer_url)

app = Flask(__name__)

a = {'Beers': beers, 'Website': beer_url}

df = pd.DataFrame.from_dict(a, orient='index')
def make_clickable(val):
    # target _blank to open new window
        return '<a target="_blank" href="{}">{}</a>'.format(val, val)

df.style.format({'Website': make_clickable})

html = (df.transpose())

@app.route("/", methods=("POST", "GET"))
def html_table():
    return html.to_html(header="true", table_id="table")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
   

#if __name__ == "__main__":
#    if APP_ENV == "development":
#        zip_code = zip_code
 #       results = get_beer() # invoke with custom params
  #  else:
   #     results = get_beer() # invoke with default params
    
    #text_file = open("index.html", "w")
    #text_file.write(results)
    #text_file.close()

#print(results)