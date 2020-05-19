#iterable data types are 
# -> string, dictionary, list, tuple, set

dict_items = {
 'name' : 'Mishan',
 'surname' : 'Regmi',
 'age': 20
}

for i in dict_items:
 print (i) # Prints keys

for i in dict_items.values():
 print(i) #Print the values of dictionary

for i in dict_items.keys():
 print(i) #Prints the key 

for i in dict_items.items():
 print(i) #Prints all the dictionary

#Print simply without tuple
for key, value in dict_items.items():
 print(key, value) #Prints simply without printing as tuple


#Using enumerate
name = 'My name is Mishan'
for chars in enumerate(name):
 print(chars) # Shows each string value with its index

for i, char in enumerate(list(range(0,25))):
 print (i, char)