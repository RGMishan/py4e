
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
