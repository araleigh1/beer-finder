from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

#
# INITIALIZE THE DRIVER
#

zip_code = input("PLEASE INPUT A ZIP CODE (e.g. 06510): ")

CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe" # (or wherever yours is installed)

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# ... OR IN "HEADLESS MODE"...
# options = webdriver.ChromeOptions()
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

#
# NAVIGATE TO GOOGLE.COM...
#

driver.get("https://www.beermenus.com/places")
print(driver.title) #> Google
#
# FIND AN ELEMENT TO INTERACT WITH...
# a reference to the HTML element:
# <input title="Search">

searchbox_xpath = '//*[@id="location_address"]'
searchbox = driver.find_element_by_xpath(searchbox_xpath)

#
# INTERACT WITH THE ELEMENT
#



search_term = zip_code
searchbox.click()


searchbox.send_keys(Keys.CONTROL,"a", Keys.DELETE)
searchbox.send_keys(search_term)
searchbox.send_keys(Keys.RETURN)
time.sleep(2)
searchbox.send_keys(Keys.RETURN)
time.sleep(1)
searchbox.send_keys(Keys.RETURN)
print(driver.title) #> 'Prof Rossetti GitHub - Google Search'
driver.save_screenshot("search_results.png")

#
# ALWAYS QUIT THE DRIVER
#

