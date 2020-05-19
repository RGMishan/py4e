dictionary = {
 'name' : 'Mishan',
 'age' : 21,
 'height' : 5.6,
}

print(dictionary) #print dictionary
print(dictionary['age']) # print existing key's value
print(dictionary.get('weight')) #check if the key naming weight is there or not
print(dictionary.get('weight',73)) # check if weight is there or not if not assign 73
print(dictionary.get('name', 'Regmi')) # check name if not found create and assign Regmi

# Another way to create dictionary
dictionary2 = dict(name="Mishan", age = 20)
print(dictionary2)

#Checking in Dictionary
print('height' in dictionary)
#Check the key
print('age' in dictionary.keys())
#Check the Values
print(18 in dictionary.values())
print(5.6 in dictionary.values())
#Check Items
print(dictionary.items())
#Clearing
print(dictionary.clear())
print(dictionary) # Shows empty after clearing
#Copying from Dictionary
dictionary = {
 'name' : 'Mishan',
 'age' : 21,
 'height' : 5.6,
 'sex' : 'male',
 'education' : 'Bachelor'
}
copied = dictionary.copy()
print(copied)
#Remove from dictionary
print(copied.pop('name')) # remove selected key and value
print(copied.popitem()) #remove last item
print(copied)
print(copied.update({'age' : 30})) #If key exists update its value
print(copied)
print(copied.update({'status' : 'happy'})) #If key doesn't exists add key & value
print(copied)
