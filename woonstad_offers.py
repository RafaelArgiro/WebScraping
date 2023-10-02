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
# -------------------- General constants and parameters
# ------------------------------------------------------------------

# File save settings
save_file   = False

# Get current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify directory for saving and recovering scraped data
directory   = 'Woonstad_Offer_Data'


# ------------------------------------------------------------------
# -------------------- Scrape offers from Woonstad
# ------------------------------------------------------------------


# Web-addresses to scrape
url = 'https://www.woonstadrotterdam.nl/api/Offers/SearchVshOfferings?sort=default&page=1&size=100&otype='

# Get data
response = requests.get(url)

# Check response status
print_section()
print("Status code: " + str(response.status_code))
print_section()

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
# -------------------- Read data from previous scrape
# ------------------------------------------------------------------

# Construct file name
file_name = 'Test2.txt'

# Construct full path to previous file
full_path = os.path.join(current_dir, directory, file_name)

# Read in previous offer data as panda DataFrame
offers_previous = pd.read_csv(full_path, index_col=0)


# ------------------------------------------------------------------
# -------------------- Checking if data is the same
# ------------------------------------------------------------------

# Transpose data
offers_df       = offers_df.transpose()
offers_previous = offers_previous.transpose()

# Convert Float data to string data in newly scraped data
offers_df['Price'] = offers_df['Price'].astype('str')
offers_df['ServiceCosts'] = offers_df['ServiceCosts'].astype('str')
offers_df['TotalPrice'] = offers_df['TotalPrice'].astype('str')

# Convert replace nan data with 'nothing'
offers_previous['Campaign'] = offers_previous['Campaign'].astype('str')
offers_previous['Campaign'] = offers_previous['Campaign'].replace('nan', '')

# Transpose data back
offers_df       = offers_df.transpose()
offers_previous = offers_previous.transpose()

# Check if newly scraped data is the same as previous data
data_is_different = not offers_df.equals(offers_previous)

print("Data different from previous scrape: " + str(data_is_different))



# ------------------------------------------------------------------
# -------------------- Save to text file
# ------------------------------------------------------------------

# Get date and time stamp
datetime_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Format datetime string
datetime_str = datetime_str.replace(':', '.')
datetime_str = datetime_str.replace(' ', '_')
datetime_str = datetime_str.replace('-', '.')

# Construct file name
file_name = 'Offers_' + datetime_str + '.txt'

# Construct full path
file_path = os.path.join(current_dir, directory, file_name)
# file_path = os.path.join(current_dir, directory, 'Test.txt')

# Determine if data must be saved
save_data   = data_is_different and save_file

# Save offer data to '.txt' file in csv format (if new data is different from previous scrape )
if save_data:
    offers_df.to_csv(file_path, sep=',')

# Print if data has been saved:
print("Data has been saved: " + str(save_data))
print_section()