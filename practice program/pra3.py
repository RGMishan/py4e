#Question 3: Accept string from a user and display only those
#characters which are present at an even index number.

def string(str1):
 for i in range(0, len(str1)-1, 2):
  print("index", i , "=", str1[i])

inputStr = input("Enter the string:")
print("The string is", inputStr)

print("The Even Index Character Are ")
string(inputStr)
