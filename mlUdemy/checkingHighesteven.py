#Checking Highest Even

def highest_even(args):
 even = []
 for i in args:
  if i % 2 == 0: #selection of only even from the list
   even.append(i)
 return max(even) #selecting max from the seven list

print("The highest even is :", highest_even([10,2,3,5,11]))
