#a short implementation of shocket
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
#above line is similar to when we use open file dont read data but go to url and fetch the file and comes

for line in fhand:
 print(line.decode().strip())

# now treating like a file
