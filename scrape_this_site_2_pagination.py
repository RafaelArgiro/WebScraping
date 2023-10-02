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

# # Web-address to scrape
# url = 'https://www.scrapethissite.com/pages/forms/?page_num=1'

# # Get data
# response = requests.get(url)

# # Check response status
# print("Status code: " + str(response.status_code))

# # Parse the HTML content using BeatifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# # Extract pagination section
# pagination  = soup.find('ul', class_ = 'pagination')

# # Find total nr of pages
# nr_of_pages = len(pagination.find_all('li')) - 1


# ------------------------------------------------------------------
# -------------------- Use for-loop to scrape all pages
# ------------------------------------------------------------------

# # Base web-address to scrape
# base_url = 'https://www.scrapethissite.com/pages/forms/?page_num='

# for ii in range(1, nr_of_pages + 1):
#     print(ii)

#     url = base_url + str(ii)
#     print(url)

#     response = requests.get(url)
#     print("Status code: " + str(response.status_code))



# ------------------------------------------------------------------
# -------------------- Use while loop to scrape all pages
# ------------------------------------------------------------------

# Base web-address to scrape
base_url = 'https://www.scrapethissite.com/pages/forms/?page_num='

# Initialize counter:
ii = 1

while True:

    # Construct and print url to extract
    url = base_url + str(ii)
    print(url)

    # Pull web-data using requests and print status
    response = requests.get(url)
    print("Status code: " + str(response.status_code))

    # Parse data using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the next button in html data
    next_button = soup.find_all('span')

    # If final page has been reached: only 1 instance of "span" is found
    if ii > 1 and len(next_button) < 2:
        # break while loop when last page has been reached
        break

    # Increase iterator
    ii = ii + 1

