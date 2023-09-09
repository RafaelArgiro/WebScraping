import requests
from bs4 import BeautifulSoup

url = 'https://www.woonstadrotterdam.nl/aanbod/vrijesector-huurwoningen?sort=default'

html = requests.get(url)

# print(html.text)
# print(html.content)

s = BeautifulSoup(html.content, 'html.parser')

# results = s.find_all('div')
# print(results)

offerings = s.find_all('ul') #, class_ = 'card-details')
print(offerings[0])

# for job in job_title:
	# print(job.text)

# print(job_title[0].text)