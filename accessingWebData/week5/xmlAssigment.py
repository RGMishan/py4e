import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# file reading is 
#   http://py4e-data.dr-chuck.net/comments_494585.xml

url = input("Enter the URL:")
xml = urllib.request.urlopen(url).read()

print ("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print ("Count: " + str(len(counts)))

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print ("Sum:" + str(accumulator))