import re

y = "From university.mishanregmi@mis.un.in Sat Jun $5 02:15:45 2020"

p = re.findall('\S+@\S+' ,y)
# \S denote non blank character + denote one or more character and @ sign in middle and again \S until last
# so its i@m but greedynesspush on both side
print (p) #prints out ['university.mishanregmi@mis.un.in']

q = re.findall('\S+?@\S+?' ,y)
print (q)

# Start extraction from specific point like after 'From '
r = re.findall('^From (\S+@\S+)' ,y) 
print (r)  #Prints same ['university.mishanregmi@mis.un.in']

s = re.findall('@([^ ]*)',y) #Start extracting from @ sign until the blank character OR everything but no space
print(s) #Prints ['mis.un.in']

t = re.findall('[a-z0-9]+' ,y)
print (t) #['$5']