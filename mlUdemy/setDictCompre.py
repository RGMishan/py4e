#set comprehension

mySet = {num for num in 'hello'}
mySet2 = {num for num in range(0,15)}
mySet3 = [num*3 for num in range(0,10) if num%2 == 0]
print(mySet)
print(mySet2)
print(mySet3)

#dictionary comprehension
myDisc = {
 'name' : 22,
 'age' : 21
}

myDict = {key:value**2 for key,value in myDisc.items() }
# or we can do myDict = {k:v**2 for k,v in myDisc.items() }
myDict2 = {key:value**2 for key,value in myDisc.items() if value % 2 == 0}
print(myDict)
print(myDict2)

myNew = {num:num*2 for num in [1,2,3]}
print(myNew)