#using beautiful soup to parse xml and HTML

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the URL:")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrive all the anchor tags
tags = soup('a')
for tag in tags:
 print(tag.get('href', None))

 #used beautiful soup to bring the list of anchor tag from the HTML