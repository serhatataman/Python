import sys
from bs4 import BeautifulSoup

# NAVIGABLE STRING OBJECTS
# NavigableString objects are the strings that are contained within a tag.

soup_object = BeautifulSoup('<h1 attribute_1 = "Heading Level 1">Future Trends in IoT in 2018</h1>', 'html.parser')

tag = soup_object.h1

print("\nTag object type: " + str(type(tag)))
print("Tag name: " + str(tag.name))

print("\nTag content: " + str(tag.string))
print("tag.string object type: " + str(type(tag.string)))

our_navigable_string = tag.string

# Replace the content of the tag with the new string
our_navigable_string.replace_with('NaN')
print("\nNew content of the tag: " + str(tag.string))


# UTILIZING NAVIGABLE STRING OBJECTS

# read html file into a string
our_html_document = open("../html.txt", 'r').read()
our_soup_object = BeautifulSoup(our_html_document, 'html.parser')

print("\nAll strings in the html document: ")
for string in our_soup_object.stripped_strings:
    print(repr(string))

# print out the first link in the html document
first_link = our_soup_object.a
print("\nFirst link in the html document: " + str(first_link))

# Parent tag of the first link
print("Parent tag of the first link: " + str(first_link.parent))

print("String content of the link: " + str(first_link.string))
print("Parent of the string content: " + str(first_link.string.parent))


