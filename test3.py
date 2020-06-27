import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver as webdriver
import pandas as pd
import time
from bs4 import BeautifulSoup


def get_results(search_term):
        global df
        url = "https://investor.dn.no/#!/NorgesAksjer/"       
        CHROMEDRIVER_PATH = r"\users\araleigh\webdrivers\chromedriver.exe"
        browser = webdriver.Chrome(CHROMEDRIVER_PATH)
        browser.get(url)
        search_box = browser.find_element_by_id("ar-search-input")
        search_box.send_keys(search_term)
        time.sleep(3)
        browser.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, search_term))).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,  
                     "//*[@id='dninvestor-content']/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div/div[1]/a"))).click() # 
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, 
                     "//*[@id='dninvestor-content']/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div/table/tbody/tr[101]/td[1]/a"))).click() 
        time.sleep(5)
        result = []
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        for posts in soup.findAll('div',{'class':'col-xs-12 ng-scope'}):
            for tr in posts.findAll('tr')[1:]:
                sh = [td for td in tr.stripped_strings]
                result.append(list(sh))
                df = pd.DataFrame(result)
        return result
final_result = []
names = ['name1', 'name2', 'name3']
for name in names:
    final_result.append(get_results(name))