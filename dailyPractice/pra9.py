#Question 9: Reverse a given number and return true if it is the same as the original number

numberS = input('Enter a number: ')
number = int(numberS)
print("Original number", number)
originalNum = number
reverseNum = 0
 
while (number > 0):
    reminder = number % 10
    reverseNum = (reverseNum * 10) + reminder
    number = number // 10
if (originalNum == reverseNum):
    print("\nThe number are same.")
else:
    print("\nThe number are different.")

