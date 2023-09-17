import requests
from bs4 import BeautifulSoup

# Tutorial adress:
# https://www.geeksforgeeks.org/python-web-scraping-tutorial/

# Making a GET request
url = 'https://www.geeksforgeeks.org/python-programming-language/'
r = requests.get(url)
 
# check status code for response received
# success code - 200
print(r)

# print url
print(r.url)

# print status code
print(r.status_code)
 
# print content of request
# print(r.content)


# -------------------- Parsing the HTML with beautiful soup

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')



# -------------------- Print some simple things

# Print the content using prettify
# print(soup.prettify())

# Print the title tag
# print(soup.title)

# Print the name of the tag
# print(soup.title.name)

# Print the name of the parent tag
# print(soup.title.parent.name)




# -------------------- Finding things

# Find the content of all the articles on the main page
# s = soup.find('div', class_='entry-content')
# content = s.find_all('p')
# print(content)

# Finding by id and getting the leftbar
# s = soup.find('div', id= 'main')
# leftbar = s.find('ul', class_='leftBarList')
# content = leftbar.find_all('li')
# print(content)




# -------------------- Finding things and extracting text

# Find the content of all the articles on the main page and extract the text
# s = soup.find('div', class_='entry-content')
# lines = s.find_all('p')
# for line in lines:
#     print(line.text)

# Find the content of all the articles on the main page and extract the text
# s = soup.find('div', id= 'main')
# leftbar = s.find('ul', class_='leftBarList')
# lines = leftbar.find_all('li')
# for line in lines:
#     print(line.text)



# -------------------- Finding all links

# find all the anchor tags with "href"
# for link in soup.find_all('a'):
#     print(link.get('href'))



# -------------------- Finding all images

# images_list = []
 
# images = soup.select('img')
# for image in images:
#     src = image.get('src')
#     alt = image.get('alt')
#     images_list.append({"src": src, "alt": alt})
     
# for image in images_list:
#     print(image)


# -------------------- Looping over multiple pages


URL = 'https://www.geeksforgeeks.org/page/'
 
for page in range(1, 10):
 
    req = requests.get(URL + str(page) + '/')
    soup = BeautifulSoup(req.text, 'html.parser')
 
    titles = soup.find_all('div', attrs={'class', 'head'})
    print(page)
    # print(titles)
    for i in range(4, 19):
        if page > 1:
            print(f"{(i-3)+page*15}" + titles[i].text)
        else:
            # print(f"{i-3}" + titles)
            print('hoi')