#map useful function
'''
#ORIGINAL
def multiple(li):
 new = []
 for items in li:
  new.append(items*2)
 return new

print(multiple([1,2,3]))
'''
def multiple(li):
 return li * 2
 #no need of any calculation when we use map

print(list(map(multiple, [4,5,6]))) #gives data and the map get act upon the function
# map knows that multiple is function so we dont even need to call it
my_list = [5,6,7] #made a new list
print(list(map(multiple, my_list)))  #called a new list print new value
print(my_list) #doesnt change the value as that was a pure function and it doesnt effect outside world
