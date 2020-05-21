'''
Python while checking for the scope of the variable in any program

1st Check by starting in local 
2nd Check the parent have the variable (in function)
3rd Check for the global variable
4th Assign the built in return function when built in fucntion are defined
'''

#Using Global Keyword
total = 0
def count():
  global total
  total += 1  # here the keyword global total value as 0
  return total

count()
print(count()) #prints 2

#Method 2
total1 = 0
def count(total1):
  total1 += 1  # here the keyword global total value as 0
  return total1

print(count(count(count(total1)))) #print 3