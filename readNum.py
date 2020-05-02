num = 0
total = 0.0
while True :
    take = input("Enter the number:")
    if take == 'done' :
        break
    try:
        ta = float(take)
    except:
        print("Invalid Value")
        continue
    print (ta)
    num = num + 1
    total = total + ta


print("Calculating")
print("Total: ", total, "Numbers: ", num,"Average: ", total/num)



largest = None
smallest = None
n = []
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        n.append(float(num))
    except:
        print("Invalid input")
        continue



for value in n:

    if value < smallest:
        smallest = value


    if smallest is None:
        smallest = value

    elif value > largest:
        largest=value


print("Maximum is", largest)
print("Minimum is", smallest)
