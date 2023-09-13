import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

# https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-23.php
# https://www.whatismybrowser.com/guides/the-latest-user-agent/edge

url     = 'https://www.imdb.com/chart/top/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'}

# Get data from webpage
html    = requests.get(url, headers=headers)
html.raise_for_status()

# Parse data into html format
soup    = bs(html.text, 'html.parser')

# movies = soup.find('tbody', class_='lister-list').find_all('tr')


print(soup.text)
