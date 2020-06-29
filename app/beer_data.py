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






CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe"
chrome_options = Options()

chrome_options.add_argument("--headless")
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get("https://www.beeradvocate.com/beer/top-new/")
time.sleep(3)
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
driver.quit()

dfs = pd.read_html(soup)
for df in dfs:
    print(df)

exit()
beer_name = []
brewery_name = []
rating = []





#table = soup.find('table')
#table_rows = table.find_all('tr')
#for tr in table_rows:
 #   td = tr.find_all('td')
  #  row = [i.text for i in td]
#print(row)



driver.quit() 
exit()

beer_div1 = soup.find_all('td', align = 'left', valign='top')


for d in beer_div1:
    divs1 = d.find_all('a')
    for z in divs1:
        bold = z.find_all('b')
        for bb in bold:
            name = bb.find_all(text=True, recursive=False)
            b = [e.strip() for e in name]
            for a in b:
                beer_name.append(str(a))
for b in beer_div1:
    muted = b.find_all('span', class_ = 'muted')
    for w in muted:
        anchor = w.find_all('a')
        for brew in anchor:                
            brewery = brew.find_all(text=True, recursive=False)
            f = [g.strip() for g in brewery]
            for aa in f:
                    brewery_name.append(str(aa))






#for rate in beer_div1:
 #   b_rate = rate.parent.find_all('td')[3]
  #  ratings = b_rate.get_text()
   # rating.append(float(ratings))

l1 = beer_name
l2 = brewery_name
l3 = rating
s1 = pd.Series(l1, name='Beer')
s2 = pd.Series(l2, name='Brewery')
s3 = pd.Series(l3, name ='Rating')
beer_df = pd.concat([s1,s2,s3], axis=1)

print(beer_df)

driver.quit()    

beer_df.to_csv('rate.csv')


#print(len(beer_name))
#print(len(brewery_name))
#print(len(rating))
#rate_df = pd.DataFrame({
 #   "Beer":beer_name,
  #  "Brewery":brewery_name,
   # "Rating":rating
#})

#print(rate_df)
   
    

