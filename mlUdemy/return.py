#Using return

#1st Way
def sum(num1,num2):
 return num1 + num2
 print('Hello')  #Return function dont allow other code to execute

total = sum(10,5) #function return here
print("Total 1 is ",sum(4,total)) # then we use the total

#2nd WAY

def sum2(num1,num2):
 def another(num1,num2):
  return num1 + num2
 return another

total2 = sum2(10,20)
print("Total 2 is :", total2(10,25))

#3rd WAY

def sum3(num1,num2):
 def another(n1,n2):
  return n1 + n2
 return another(num1,num2)

total2 = sum3(10,20)
print("Total 2 is :", total2)
