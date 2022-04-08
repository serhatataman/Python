from bs4 import BeautifulSoup

import urllib
import urllib.request
import re


# DATA PARSING

with urllib.request.urlopen("https://raw.githubusercontent.com/BigDataGal/Data-Mania-Demos/master/IoT-2018.html") as response:
    html = response.read()


soup = BeautifulSoup(html, 'html.parser')

print("\nInput type" + str(type(soup)))
print("\nHttp document: " + str(soup.prettify()[0:100]))

# Getting data from parse tree
# Print out all the string content inside the tags
text_only = soup.get_text()
print("Text only: " + str(text_only))

# SEARCHING AND RETRIEVING DATA FROM PARSE TREE

# Retrieve tags by filtering with name arguments
print("\nRetrieve tags by filtering with name arguments: " + str(soup.find_all('li')))

# Retrieve tags by filtering with keyword arguments
print("\nRetrieve tags by filtering with keyword arguments: " + str(soup.find_all(id='link 7')))

# Retrieve tags by filtering with string arguments
print("\nRetrieve tags by filtering with string arguments: " + str(soup.find_all('ol')))

# Retrieve tags by filtering with list objects
print("\nRetrieve tags by filtering with list objects: " + str(soup.find_all(['ol', 'b'])))

# Retrieve tags by filtering with regular expression
t = re.compile("t")
for tag in soup.find_all(t):
    print("Retrieve tags by filtering with regular expression: " + str(tag))

# Retrieve weblinks by filtering with string objects
for link in soup.find_all('a'):
    print("Retrieve weblinks by filtering with string objects: " + str(link.get('href')))


# Retrieve strings by filtering with regular expression
print("\nRetrieve strings by filtering with regular expression: " + str(soup.find_all(string=re.compile("data"))))



