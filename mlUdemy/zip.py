#zip function

myList= [1,2,3]
urList= [4,5,6]

print(list(zip(myList,urList))) # create a list of tupples
# store one one iterable from both the list or itearable
# prints out [(1, 4), (2, 5), (3, 6)]

myList2= [1,2,3,5,6]
urList2= (4,5,6)  #doesnot matter if it is list or tupple need to be iterable

print(list(zip(myList2,urList2))) #prints out same input until it finds out its same iterable

#can be used in database to get info of name and phone number related and create new set
#can add as many iterable you want