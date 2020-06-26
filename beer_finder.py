from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

zip_code = input("PLEASE INPUT A ZIP CODE (e.g. 06510): ")

# Searching BeerMenues by Zipcode
CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get("https://www.beermenus.com/places")
searchbox_xpath = '//*[@id="location_address"]'
searchbox = driver.find_element_by_xpath(searchbox_xpath)
search_term = zip_code
searchbox.click()
searchbox.send_keys(Keys.CONTROL,"a", Keys.DELETE)
searchbox.send_keys(search_term)
searchbox.send_keys(Keys.RETURN)
time.sleep(2)
searchbox.send_keys(Keys.RETURN)
time.sleep(1)
searchbox.send_keys(Keys.RETURN)