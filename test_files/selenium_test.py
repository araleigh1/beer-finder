from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#
# INITIALIZE THE DRIVER
#

CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe" # (or wherever yours is installed)

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# ... OR IN "HEADLESS MODE"...
# options = webdriver.ChromeOptions()
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)


driver.get("https://www.beermenus.com/places")
print(driver.title) #> Google

#
# FIND AN ELEMENT TO INTERACT WITH...
# a reference to the HTML element:
# <input title="Search">

searchbox_xpath = '//*[@id="location_latitude"]'
searchbox = driver.find_element_by_xpath(searchbox_xpath)

#
# INTERACT WITH THE ELEMENT
#

search_term = "Prof Rossetti GitHub"
searchbox.send_keys(search_term)

searchbox.send_keys(Keys.RETURN)
print(driver.title) #> 'Prof Rossetti GitHub - Google Search'


#
# ALWAYS QUIT THE DRIVER
#

driver.quit()