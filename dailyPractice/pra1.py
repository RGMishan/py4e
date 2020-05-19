#Question 1: Accept two integer numbers from a user and return their 
#product and  if the product is greater than 1000, then return their sum

int1 = input("Input first number:")
int2 = input("Input second number:")

tot = int(int1) * int(int2)
print("Product =", tot)

if tot > 1000:
  pro = int(int1) + int(int2)
  print("Sum =", pro)