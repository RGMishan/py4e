'''
#Unique pair of elements
my_sets = {1,2,3,4,5}
print(my_sets)

#No Duplicate will be counted
my_sets2 = {1,2,3,4,5,5}
my_sets2.add(2)
my_sets2.add(100)
print(my_sets2)

#COnverting list into set
myList = [1,2,3,3,2]
print(myList)
mySet = set(myList)
print(mySet)

#Checking a value in set

#print(my_sets[0]) # this gives traceback error
print(1 in my_sets)

#Calculating length
print(len(mySet)) #doesnot count the recurring value

#Copying
mySet2 = mySet.copy()
print(mySet2) #display only unique element

#Clearing Set
print(mySet2.clear()) # prints -> None

'''

my_set = {1,2,3,4,5}
ur_set = {4,5,6,7,8,9}

#Check Difference in Sets
print(my_set.difference(ur_set)) # {1, 2, 3}

#Removing element
print(my_set.discard(1)) # print None
print(my_set) #print  {2, 3, 4, 5}

#Difference and then update
print(my_set.difference_update(ur_set)) #print None
print(my_set) #print {2, 3}

#Now we Update our set after all the operation
my_set2 = my_set = {1,2,3,4,5}

#Intersection in the Sets
print(my_set2.intersection(ur_set)) # Output {4, 5}

#Disjoint
print(my_set2.isdisjoint(ur_set)) #Return False as they are not disjoint\

#Checking Subset
test1 = {1,2,3}
test2 = {2,3}
print(test2.issubset(test1)) #Returns True

#Checking Superset
print(test1.issubset(test2)) #Returns True

#Union of 2 Sets
uni = my_set2.union(ur_set)
print(uni) # Prints {1, 2, 3, 4, 5, 6, 7, 8, 9}


# SOme SHortcut

print(my_set2 | ur_set) # This also print union 
print(my_set2 & ur_set) # This also print intersection 
