#Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

my_list = [1,5,6,10,14,13,20]

i = 0
new_lst = []
for i in my_list:
 if i % 5 == 0:
  print(i)
  new_lst.append(i)
print(new_lst)