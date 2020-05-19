import re
dFile = open('file.txt')

numlist = list()
sum = 0

for lines in dFile:
 numbers = re.findall('[0-9]+', lines)
 if not numbers:
  continue
 else:
  for number in numbers:
   sum += int(number)
print(sum)
