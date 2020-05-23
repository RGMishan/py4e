#list set dictionary comprehension
myList = []

for char in 'Whats up?':
 myList.append(char)
print(myList)

#myList = [param in param for iterable]
myList1 = [char for char in 'hello'] #for each varible in the iterable add it to the list
myList2 = [num for num in range(0,10)]
myList3 = [num*3 for num in range(0,10)]
myList4 = [num*3 for num in range(0,10) if num%2 == 0]
#myList = ["what we want to do" "we loop through the iterable" "condition added"]
print(myList1)
print(myList2)
print(myList3)
print(myList4)
