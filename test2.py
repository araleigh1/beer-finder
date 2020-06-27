import requests
from bs4 import BeautifulSoup
import re

page = requests.get("https://in.udacity.com/courses/all")
soup = BeautifulSoup(page.content, 'html.parser')
courses = soup.find_all("a", class_="capitalize")
search_term = "AI"

for course in courses:
    if re.search(search_term, course.text, re.IGNORECASE):
        print(course.text)
        