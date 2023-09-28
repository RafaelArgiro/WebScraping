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
    print('==========================================================================')
    print()

def print_section():
    # Print section separator
    print()
    print('_____________________________________')
    print()


# ------------------------------------------------------------------
# -------------------- Scrape offers from Woonstad
# ------------------------------------------------------------------


# Web-addresses to scrape
url = 'https://www.woonstadrotterdam.nl/api/Offers/SearchVshOfferings?sort=default&page=1&size=100&otype='


# Get data
response = requests.get(url)

# Check response status
print()
print("Status code: " + str(response.status_code))
print()


# Parse data
data    = response.json()

# print(type(data))
# print(data)

# print_header()
# print('data[SubTypes]')
# print_section()
# print(data['SubTypes'])

# print_header()
# print('data[Filters]')
# print_section()
# print(data['Filters'])

# list__ = list(data)

# key = 'SubTypes'

# print_header()
# print(list__[list__.index(key) + 4])


print_header()
print('data[Items]')
print_section()
print(data['Items'])
print(len(data['Items']))
print(type(data['Items']))
print(data['Items'][0])
print(type(data['Items'][0]))

# print_header()
# print('data[Data]')
# print_section()
# print(data['Data'])

# print_header()
# stuff = data['Items']
# print(type(stuff[0]))
# stuff_json = json.dumps(stuff[0], indent=4)
# print(type(stuff_json))
# print(stuff_json)







