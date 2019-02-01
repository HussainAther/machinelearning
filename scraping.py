"""
To scrape a website, we use an “Extractor”, as import.io calls it, to create a graphical interface. It has two tabs: “Edit” will display the website. Import.io analyses the website’s structure and automatically tries to find and highlight structured information for extraction. If it didn't select the correct information , you can easily change the selection by clicking on the website’s elements you are interested in.
"""

import requests
from bs4 import BeautifulSoup as bs


response = requests.get("http://weihnachtsmarkt-deutschland.de")
print(response.text)

soup = bs(response.text,'lxml')

rows = soup.find_all('tr')
print(rows)
