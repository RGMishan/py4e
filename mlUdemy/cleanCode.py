#clean code
def is_even(num):
 if num % 2 == 0:
  return True
 elif num % 2 != 0:
  return False

print(is_even(51)) 

#cleaned code
'''
# No need of elif if we are checking for even odd
if num % 2 == 0:
  return True
 else:
  return False
# no need of else statement just return True if 'if loop' get executed
if num % 2 == 0:
  return True
 return False
# no need to use loop if we are checking boolean value we can just check
   return num % 2 == 0
'''

def is_even1(num):
 return num % 2 == 0
print(is_even1(24))
