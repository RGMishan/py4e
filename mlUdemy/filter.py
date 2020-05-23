#filter function

def only_odd(item):
 return item % 2 == 1 #works on the boolean expression

print(list(filter(only_odd , [1,23,2,4,5]))) # filter out values what the function wants
# the filter gave output to those number only which satisfy the function condition