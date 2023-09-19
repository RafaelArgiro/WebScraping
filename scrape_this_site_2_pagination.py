import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from pprint import pprint


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
# -------------------- Scrape first page to determine the total nr of pages
# ------------------------------------------------------------------

# Web-address to scrape
url = 'https://www.scrapethissite.com/pages/forms/?page_num=1'

# Get data
response = requests.get(url)

# Check response status
print("Status code: " + str(response.status_code))

# Parse the HTML content using BeatifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract pagination section
pagination  = soup.find('ul', class_ = 'pagination')

# Find total nr of pages
nr_of_pages = len(pagination.find_all('li')) - 1


# ------------------------------------------------------------------
# -------------------- Use for-loop to scrape all pages
# ------------------------------------------------------------------

# Base web-address to scrape
base_url = 'https://www.scrapethissite.com/pages/forms/?page_num='

for ii in range(1, nr_of_pages + 1):
    print(ii)

    url = base_url + str(ii)
    print(url)

    response = requests.get(url)
    print("Status code: " + str(response.status_code))




# # ------------------------------------------------------------------
# # -------------------- Navigation pane
# # ------------------------------------------------------------------

# # Find the navigation pane data from web data
# # nav_tabs = soup.find('ul', class_ = 'nav nav-tabs')
# # print(nav_tabs)
# # print_section()

# # Find all hyperlinks within navigation pane
# # The links are under the "a" tag in the nav_tabs object
# # nav_pane_links = nav_tabs.find_all('a')
# # print(nav_pane_links)
# # print_section()

# # Actual links are under the "href" tag
# # Use .get('href') method to get the actual links
# # for link in nav_pane_links:
#     # print(link.get('href'))
# # print_section()


# # ------------------------------------------------------------------
# # -------------------- Title and header
# # ------------------------------------------------------------------
# # Find the title and description from web data

# # Find the information in the page class
# # page = soup.find('div', id = 'page')
# # # Find the title and the description using the 'col-md-12' class
# # info = page.find_all('div', class_ = 'col-md-12')
# # title       = info[0]
# # description = info[1]
# # # Print results
# # print(title.text.strip())
# # print(description.text.strip())


# # ------------------------------------------------------------------
# # -------------------- Countries
# # ------------------------------------------------------------------
# # Find the information on all countries listed

# # Find all countries using class "col-md-4 country"
# countries = soup.find_all('div', class_ = 'col-md-4 country')

# # Print the total nr of countries found
# print("Number of countries found: " + str(len(countries)))
# print_section()

# countries_list = []

# for country in countries:
#     # Extract information for all countries
#     name        = country.find('h3')
#     capital     = country.find('span', class_ = 'country-capital')
#     population  = country.find('span', class_ = 'country-population')
#     area        = country.find('span', class_ = 'country-area')
#     # Convert to strings
#     name       = name.text.strip()
#     capital    = capital.text.strip()
#     population = population.text.strip()
#     area       = area.text.strip()
#     # Add information to countries list
#     list_ii     = [name, capital, population, area]
#     countries_list.append(list_ii)


# # Create table from data
# headers_ = ['Country', 'Capital', 'Population', 'Area']
# table = tabulate(countries_list, headers = headers_)
# print(table)
# print_section()

