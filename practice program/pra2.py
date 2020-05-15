#Question 2: Given a range of first 10 numbers, Iterate from start number to
#the end number and print the sum of the current number and previous number

num = 10 
prev = 0
print("Printing current and previous number sum in a given range(10)")
for i in range(num):
 tot = i + prev
 print("Current num =", i,"Previous num =", prev, "Sum =", tot)
 prev = i