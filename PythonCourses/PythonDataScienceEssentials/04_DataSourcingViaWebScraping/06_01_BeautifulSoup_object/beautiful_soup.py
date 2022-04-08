import sys
from bs4 import BeautifulSoup

# BEAUTIFUL SOUP

# read html file into a string
our_html_document = open("../html.txt", 'r').read()

# By default BeautifulSoup has utf-8 formatting, convert it to unicode formatting
our_soup_object = BeautifulSoup(our_html_document, 'html.parser')
# print first 300 characters of the html document, prettified
print(our_soup_object.prettify()[0:300])


# TAG OBJECTS

# Pull the tag from html document, as lxml markup
soup_object = BeautifulSoup('<h1 attribute_1 = "Heading Level 1">Future Trends for IoT in 2018</h1>', 'html.parser')

tag = soup_object.h1

print("Tag type: " + str(type(tag)))
print("The tag: " + str(tag))
print("Tag name: " + str(tag.name))

# Change the tag name
tag.name = "heading 1"
print("The tag: " + str(tag))
print("Tag name: " + str(tag.name))


# TAG ATTRIBUTES
print("\n TAG ATTRIBUTES")
# We can access the tag's attributes by treating the tag like a Dictionary
soup_object = BeautifulSoup('<h1 attribute_1 = "Heading Level 1">Future Trends for IoT in 2018</h1>', 'html.parser')
tag = soup_object.h1

print("The tag: " + str(tag))
print("The attribute_1's value: " + str(tag['attribute_1']))

# Print all tag attributes
print("Tag attributes: " + str(tag.attrs))

# Add an attribute to attribute list
tag['attribute_2'] = "Heading Level 1"
print("Tag attributes after addition: " + str(tag.attrs))

# Remove an attribute from attribute list
del tag['attribute_2']
print("Tag attributes after deletion of attribute 2: " + str(tag.attrs))


print("\n NAVIGATING A PARSE TREE USING TAGS")
# retrieving all the tags in the html document

# get the head tag from the html document
print("Head tag: " + str(our_soup_object.head))

print("Title tag: " + str(our_soup_object.title))

# Get the title content which is within b, within body
print("Title content tag: " + str(our_soup_object.body.b))




