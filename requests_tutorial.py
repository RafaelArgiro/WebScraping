import requests

# Specify url
url = 'https://api.github.com/users/naveenkrnl'

# Making a GET request
r = requests.get(url)
  
# check status code for response received
# success code - 200
print(r)
  
# print content of request
print(r.content)