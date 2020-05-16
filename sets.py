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