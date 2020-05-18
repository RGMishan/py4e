#Finding from the string using regular expression

import re # importing library

x = "My age is 21 and I have a height of 5 foot 6 inch."

y = re.findall('[0-9]+', x) 
# here 0-9 is the values to search and + is you can look for 
# any no of digits continue and look in x

z = re.findall('[aeiou]+',x) # same thing for aeiou
print(y)
print(z)