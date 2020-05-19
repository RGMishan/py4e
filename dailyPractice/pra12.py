#Question 5: Given a list iterate it and display numbers which are
#divisible by 5 and if you find number greater than 150 stop the loop iteration

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in list1:
 if (i % 5 == 0) and (i <= 150):
  print(i)

#Question 6: Given a number count the total number of digits in a number

num = 75869
count = 0
while num != 0:
    num //= 10
    count+= 1
print("Total digits are: ", count)