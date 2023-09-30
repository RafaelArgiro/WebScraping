import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from tabulate import tabulate


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

# Parse data using json method to dict
data    = response.json()



# ------------------------------------------------------------------
# -------------------- Pre-process data
# ------------------------------------------------------------------

# Find all dict names by converting data to list object
dict_names = list(data)

# The Woonstad offers are contained in the third dict item
offers_dict_name = dict_names[2]

# Extract Woonstad offer data
offers_data = data[offers_dict_name]

# Find the number of offers
nr_of_offers = len(offers_data)

# Check with the total count from the scraped data
total_count = data[dict_names[-1]]['TotalCount']

# Raise warning if not all offers have been scraped correctly
if nr_of_offers != total_count:
    raise Warning("Number of offers scraped not equal to total nr of offers.")


# ------------------------------------------------------------------
# -------------------- Convert dict to panda
# ------------------------------------------------------------------

# Create empty DataFrame
offers_df = pd.DataFrame()

# Load all data into DataFrame
for offer in offers_data:

    # Remove 'Image' data from offer dict
    del offer['Image']

    # Get name of current offer
    name = offer['Name']
    name = name.strip()

    # Convert to pandas
    offer_df = pd.DataFrame.from_dict(offer, orient='index', columns=[name])

    # Append to DataFrame
    offers_df = pd.concat([offers_df, offer_df], axis=1)


# ------------------------------------------------------------------
# -------------------- Add names to indices of DataFrame
# ------------------------------------------------------------------



print(offers_df)
print_section()
print(offers_df['Evenaar 219'])
print_section()
print(offers_df.index[0])


# # ------------------------------------------------------------------
# # -------------------- Save to text file
# # ------------------------------------------------------------------

# Get date and time stamp
datetime_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Format datetime string
datetime_str = datetime_str.replace(':', '.')
datetime_str = datetime_str.replace(' ', '_')
datetime_str = datetime_str.replace('-', '.')

# Get current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify directory to save the file
directory = 'Woonstad_Offer_Data'

# Construct file name
file_name = 'Offers_' + datetime_str + '.txt'

# Construct full path
# file_path = os.path.join(current_dir, directory, file_name)
file_path = os.path.join(current_dir, directory, 'Offers_test.txt')


# Safe offer data to '.txt' file in csv format
offers_df.to_csv(file_path, sep=',')

