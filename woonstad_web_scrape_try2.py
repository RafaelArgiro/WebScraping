import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = 'https://www.woonstadrotterdam.nl/aanbod/vrijesector-huurwoningen?sort=default'

data    = requests.get(url)

soup    = bs(data.text, 'html.parser')

print(soup.text)