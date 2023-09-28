import requests
from bs4 import BeautifulSoup
import pandas as pd
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


# print_header()
# print('data[Items]')
# print_section()
# print(data['Items'])
# print_section()
# print('type of data: \t \t' + str(type(data['Items'])))
# print('Length of data list: \t ' + str(len(data['Items'])))
# print_section()
# print('First element of list:')
# print('Type: \t \t' + str(type(data['Items'][0])))
# print(data['Items'][0])

# ------------------------------------------------------------------
# -------------------- Convert dict to panda
# ------------------------------------------------------------------

print_header()
stuff = data['Items']
# print(stuff)

# print_header()

# print(stuff["Name"])
# print(stuff["Id"])
# print(stuff["Type"])
# print(stuff["TypeTranslated"])
# print(stuff["ObjectType"])
# print(stuff["SalesType"])
# print(stuff["Campaign"])
# print(stuff["Url"])

# Initialize with first item
PandaData = pd.DataFrame.from_dict(stuff[0], orient='index')
print(PandaData)
# PandaData = pd.DataFrame.from_dict(stuff)
# print(PandaData)

# del stuff['Image']
# print(stuff)

# # Initialize with first item
# PandaData2 = pd.DataFrame.from_dict(stuff, orient='index')
# print(PandaData2)
# PandaData2 = pd.DataFrame.from_dict(stuff, index=[0])
# print(PandaData2)


for ii in range(1, len(stuff)):
    print_section()
    
    panda_ii = pd.DataFrame.from_dict(stuff[ii], orient='index')
    PandaData = pd.concat([PandaData, panda_ii], axis=1)

PandaData = PandaData.transpose()
print(PandaData)

print_section()

print(PandaData['Name'])
    






# print_section()
# df1 = pd.DataFrame({"a":[1, 2, 3, 4],
#                     "b":[5, 6, 7, 8]})

# print(df1)
# df2 = pd.DataFrame({"a":[1, 2, 3],
#                     "b":[5, 6, 7],
#                     "c":[1, 5, 4]})

# hoi = pd.concat([df1, df2])
# print(hoi)





# print_header()
# print(PandaData)
# print()
# print(PandaData.transpose)

# print_header()
# print('data[Data]')
# print_section()
# print(data['Data'])

# print_header()
# stuff = data['Items']

# for ii in range(0, len(data['Items'])):

#     print(type(stuff[ii]))
#     stuff_json = json.dumps(stuff[ii], indent=2)
#     print(type(stuff_json))
#     print(stuff_json)








