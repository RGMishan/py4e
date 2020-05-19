#Question : Accept n number from user and calculate the sum of all number between 1 and n including n

num = input("Enter a number: ")
num = int(num)
sum = 0

for i in range(num+1):
 sum += i

print(sum)

#Question : Accept n number from user and print its multiplication table

mult = 1
for i in range(1, 11, 1):
    product = num*i
    print(num, " * ", i, " = ", product)

