#reduce function
#not a built in so need to import

from functools import reduce

myList = [2,3,5,7,11,22]

def accumulate(acc, items):
 print(acc, items)
 return acc + items
print(reduce(accumulate, myList, 0)) # function, data that we want to iterate over, initial value
print("\n")
#my list will be going through the function
# 1st thing it will print the value as our initial value is set to 0 acc is 0 and item is first item value
# then it returns the sum of the numbers 
# then the "acc value is set to returned" and itema value iterated over next value
# so we reduce our list to one
print(reduce(accumulate, myList, 10))  # you can set the initial to any value
