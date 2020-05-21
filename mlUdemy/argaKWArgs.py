# *args and **kwargs

def superSum(*args):
 print(args) # gives parameter as tuple
 print(*args) # gives all parameter
 return sum(args)
 
print(superSum(1,2,3,4))

def superSum2(*args, **kwargs):
 print(kwargs) # gives keys as dictionary 
 total = 0
 print(*kwargs) # gives all key parameter
 for items in kwargs.values():
  total += items
 return sum(args) + total #gives sum
 
print(superSum2(1,2,3,4, num1=5, num2=10)) #now it can take any positional or keyword argument as it wants

#RULE FOR GIVING PARAMETER IN FUNCTION
# def smth(parameter, *args, default parameter, **kwargs)