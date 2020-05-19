# Question 10: Given a two list of numbers create a new list such that new list
# should contain only odd numbers from the first list and even numbers from the second list

lst1 = [1, 2, 5, 9, 8, 7, 6, 3, 14]
lst2 = [2, 4, 5, 7, 8, 6, 1, 12, 11]

lst3 = []

for i in lst1:
 if (i % 2 == 1):
  lst3.append(i)

for j in lst1:
 if (j % 2 == 0):
  lst3.append(j)

print(lst3)