print ("Python")
print ("Assignment 2")

print ('Task 0')

myString = "Hello! \nWelcome to Python class on STRINGS.\nThis is our 2nd Lab class."
print (myString)

print("\nTask 1")
print("Built-in String Function")

#1 Start With
sli = myString.startswith("elc")
print(sli) #print false as the string start with Hello
#2
sli = myString.startswith("Hel")
print(sli) #print True as the string start with Hello
#3
cou = myString.count("class")
print(cou) # print 2 by counting "class" character in string
#4
fin = myString.find("on")
print(fin) # print 23 by getting the index of "on" from string
#5
myString2 = "Joining"
jon = "+".join(myString2)
print(jon) # join all character of string with (+)
#6
myString3 = "     Strip Me     "
stp = myString3.strip()
print(stp) # Remove the white space from the string