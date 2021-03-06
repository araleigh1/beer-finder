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
import os
from flask import Flask, request, render_template, session, redirect
import numpy as np

load_dotenv()

APP_ENV = "development"
CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe" #Note to user - insert your Chromedriver Path here
#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")

#https://github.com/vprusso/youtube_tutorials  - used to learn basics of webscraping
#https://stackoverflow.com/questions/44668998/selenium-how-to-get-page-source-code-after-clicking-a-button

def get_beer(zip_code):

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    driver.get("https://www.beermenus.com/places")
    searchbox_xpath = '//*[@id="location_address"]'
    searchbox = driver.find_element_by_xpath(searchbox_xpath)
    search_term = zip_code
    searchbox.click()
    searchbox.send_keys(Keys.CONTROL,"a", Keys.DELETE)
    time.sleep(2)
    searchbox.send_keys(search_term)
    time.sleep(3)
    searchbox.send_keys(Keys.RETURN)
    time.sleep(2)
    searchbox.send_keys(Keys.RETURN)
    time.sleep(2)
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

    print("-----------------------------------------------------------------------")
    print("Found "+str(len(full_url))+ " LOCAL BARS AND RESTAURANTS")
    print("Check CSV File in Data Folder for All of the Details!")
    print("-----------------------------------------------------------------------")

    beers = []
    beer_sites = []

    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)

    for u in full_url[:10]:
        browser.get(u)
        time.sleep(2)     
        response = browser.page_source
        soup1 = BeautifulSoup(response, "html.parser") 
        
        def check_id(tag):
            valid_ids = ['on_tap','cans','bottles']
            if tag.has_attr('id'):
                return tag['id'] in valid_ids
            else:
                return False              
        beer_div1 = soup1.find_all(check_id)
        for d in beer_div1:
            divs1 = d.find_all('li', class_ = 'pure-list-item')
            for z in divs1:
                containerz = z.find_all('h3', class_ = 'mb-0 text-normal')
                for container in containerz:
                    links0 = container.find_all('a')
                    for n in links0:
                        name = n.find_all(text=True, recursive=False)
                        b = [e.strip() for e in name]
                        for a in b:
                            beers.append(str(a))
                    for sites1 in links0:
                        beer_sites.append(sites1['href']) 
       
    browser.quit()

#https://medium.com/better-programming/the-only-step-by-step-guide-youll-need-to-build-a-web-scraper-with-python-e79066bd895a
#https://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python
    
    
    beer_url = [home + x for x in beer_sites]

    l1 = beers
    l2 = beer_url
    s1 = pd.Series(l1, name='Beer')
    s2 = pd.Series(l2, name='Website')
    beer_df = pd.concat([s1,s2], axis=1)
    df0 = beer_df.drop_duplicates(subset=['Beer'])
    df = df0.drop_duplicates(subset=['Website'])

    CSV_FILENAME = "beer_ratings.csv"
    csv_filepath = os.path.join("data",CSV_FILENAME)
    df2 = pd.read_csv(csv_filepath, encoding='latin1')
    total_df = pd.merge(df, df2, on='Beer', how='left')
    total_df.fillna(0, inplace=True)
    results = total_df.sort_values(by=['Rating'], ascending=False)
    results.set_index('Beer', inplace=True)
    results.index.names = [None]
    os.chdir("data")
    results.to_csv('data.csv')
    return results

#https://stackoverflow.com/questions/45051882/valueerror-arrays-must-all-be-same-length-in-python-using-pandas-dataframe?rq=1

if __name__ == "__main__":
    
    try:
        if APP_ENV == "development":
            zip_code = input("PLEASE INPUT A ZIP CODE (e.g. 06510): ")
            results = get_beer(zip_code=zip_code) # invoke with custom params
        else:
            results = get_beer() # invoke with default params
            os.chdir("data")
            results.to_csv('data.csv')
        print(results)
    except KeyError as KeyError:
        print("Oops!  Please use a valid Zip Code and Try Again!")
        exit()            