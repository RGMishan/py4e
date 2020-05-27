#using beautiful soup to parse xml and HTML

import urllib.request, urllib.parse, urllib.error
import beautifulSoup

url = input("Enter the URL:")
html = urllib.request.urlopen(url).read()
soup = beautifulSoup(html, 'html.parser')

#Retrive all the anchor tags
tags = soup('a')
for tag in tags:
 print(tag.get('href', None))