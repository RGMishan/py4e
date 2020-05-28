import xml.etree.ElementTree as ET
data = '''<person> 
   <name>Chuck</name>
   <phone type='intl'>
     +2365478924
   </phone>
   <email hide ="yes"/>
 </person>'''
#XML file that has been extracted using urlib and beautiful soup

tree = ET.fromstring(data) #use of fromstring is to take a string and give a picture of data 
print('Name:',tree.find('name').text) #find whats in the name
print('Attr:',tree.find('email').get('hide')) #finds the status of email