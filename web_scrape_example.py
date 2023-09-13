import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = 'https://www.scrapethissite.com/pages/simple/'

data    = requests.get(url)

soup    = bs(data.text, 'html.parser')

result = soup.find_all('h3', class_='country-name')

print(result)
