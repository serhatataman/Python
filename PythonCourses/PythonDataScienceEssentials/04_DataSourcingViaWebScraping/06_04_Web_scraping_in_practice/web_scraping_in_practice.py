from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re


r = urllib.request.urlopen('https://analytics.usa.gov/')
soup = BeautifulSoup(r, 'html.parser')

print("Content of the webpage: " + soup.prettify()[:100])

print("\nPrint all the links in the webpage that include http: ")
# Print only http links - not all the links
for tag in soup.find_all('a', attrs={'href': re.compile("^http")}):
    print(tag.get('href'))

# save this info into a file
file = open('parsed_data.txt', 'w')
for tag in soup.find_all('a', attrs={'href': re.compile("^http")}):
    soup_link = str(tag)
    file.write(soup_link)

file.flush()
file.close()



