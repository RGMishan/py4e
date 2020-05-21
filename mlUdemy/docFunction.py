#Documenting a function

def add(num1, num2):
 '''
 This function is to used to add two function
 ''' 
 return num1 + num2
print(add(5,2))
print(add) # it shows the documentation when you hover over add describing add function

def sub(num1, num2):
 '''
 This function is to used to subtract two function
 ''' 
 return num1 - num2
print(sub(5,2))
print(sub) # it shows the documentation when you hover over sub describing sub function

help(add) #prints add(num1, num2)  This function is to used to add two function
print(sub.__doc__) # prints     This function is to used to subtract two function