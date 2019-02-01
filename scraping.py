import requests
from bs4 import BeautifulSoup as bs
"""
To scrape a website, we use an “Extractor”, as import.io calls it, to create a graphical interface. It has two tabs: “Edit” will display the website. Import.io analyses the website’s structure and automatically tries to find and highlight structured information for extraction. If it didn't select the correct information , you can easily change the selection by clicking on the website’s elements you are interested in.
"""

response = requests.get("http://weihnachtsmarkt-deutschland.de")
print(response.text)

# Use bs to parse
soup = bs(response.text,'lxml')

rows = soup.find_all('tr')
print(rows)

for row in rows:
     print(row.text)
