import requests

query = 'Jefferson'

url = 'http://www.phillyhistory.org/historicstreets/default.aspx'
post_data = {'txtStreetName': query}

html_result =  requests.post(url, data=post_data).content

print(html_result)