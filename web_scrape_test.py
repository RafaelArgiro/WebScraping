import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url     = 'https://notes.ayushsharma.in/technology'

data    = requests.get(url)

extracted_data = []

html    = bs(data.text, 'html.parser')
articles = html.select('a.post-card')

for article in articles:

    title       = article.select('.card-title')[0].get_text()
    excerpt     = article.select('.card-text')[0].get_text()
    pub_date    = article.select('.card-footer small')[0].get_text()

    extracted_data.append({"title": title, "excerpt": excerpt, "pub_data": pub_date})

pprint(extracted_data[0])
