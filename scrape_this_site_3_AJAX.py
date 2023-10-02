import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import json


# ------------------------------------------------------------------
# -------------------- Define functions
# ------------------------------------------------------------------

def print_header():
    # Print header
    print()
    print('=====================================')
    print()

def print_section():
    # Print section separator
    print()
    print('_____________________________________')
    print()



# ------------------------------------------------------------------
# -------------------- Scrape pages using hardcoded urls from AJAX requests
# ------------------------------------------------------------------

# Web-addresses to scrape
urls = [    'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2010',
            'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2011',
            'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2012',
            'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2013',
            'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2014',
            'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2015',
            'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2016']

# Define table headers
headers_ = ['Title', 'Year', 'Awards', 'Nominations']

for url in urls:

    # Get data
    response = requests.get(url)

    # Print url:
    print_section()
    print(url)

    # Check response status
    print("Status code: " + str(response.status_code))
    print()

    # Parse to json
    response_json = response.json() 

    # Initialize movies list
    movies_list = []

    # Loop over items in reponse object
    for film in response_json:
    
        # Extract information from dicts
        title           = film["title"]
        year            = film["year"]
        awards          = film["awards"]
        nominations     = film["nominations"] 
        # Append to list
        movies_list.append([title, year, awards, nominations])

    # Create and print table
    table = tabulate(movies_list, headers = headers_)
    print(table)

