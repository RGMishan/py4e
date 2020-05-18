#Question 7: Return the total count of string “Emma” appears in the given string
#Given string is “Emma is good developer. Emma is a writer”

string = "Emma is good developer. Emma is a writer"

string_split = string.split(" ")

count = 0

for i in string_split:
 if i == 'Emma':
  count += 1

print("Emma appeared", count ,"times") 