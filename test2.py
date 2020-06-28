from bs4 import BeautifulSoup as bsoup
import requests as rq
import re

spring_2015 = "http://my.gwu.edu/mod/pws/subjects.cfm?campId=1&termId=201501"
r = rq.get(spring_2015)
soup = bsoup(r.text)
classes_url_list = [c["href"] for c in soup.find_all("a", href=re.compile(r".*courses.cfm\?campId=1&termId=201501&subjId=.*"))]
print(classes_url_list)

with open("results.txt","wb") as acct:
    for class_url in classes_url_list:
        base_url = "http://my.gwu.edu/mod/pws/{}".format(class_url)
        r = rq.get(base_url)

        soup = bsoup(r.text)
        # Use regex to isolate only the links of the page numbers, the one you click on.
        page_count_links = soup.find_all("a",href=re.compile(r".*javascript:goToPage.*"))
        try:
            num_pages = int(page_count_links[-1].get_text())
        except IndexError:
            num_pages = 1

        # Add 1 because Python range.
        url_list = ["{}&pageNum={}".format(base_url, str(page)) for page in range(1, num_pages + 1)]

        # Open the text file. Use with to save self from grief.
        for url_ in url_list:
            print("Processing {}...".format(url_))
            r_new = rq.get(url_)
            soup_new = bsoup(r_new.text)
            for tr in soup_new.find_all('tr', align='center'):
                stack = []
                for td in tr.findAll('td'):
                    stack.append(td.text.replace('\n', '').replace('\t', '').strip())
                acct.write(", ".join(stack) + '\n')