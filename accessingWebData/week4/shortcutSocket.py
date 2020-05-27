#a short implementation of shocket
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
#above line is similar to when we use open file dont read data but go to url and fetch the file and comes

#getting info from the file to run the second code this part should be comment
for line in fhand:
 print(line.decode().strip())

# now treating like a file

counts = dict()
for line in fhand:
 words = line.decode().strip()
 for word in words:
  counts[word] = counts.get(word, 0) + 1

print(counts)
