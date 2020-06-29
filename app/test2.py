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

from beer_finder import get_beer

zip_code = input("PLEASE INPUT A ZIP CODE (e.g. 06510): ")

results = get_beer(zip_code)
print(results)