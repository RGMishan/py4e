
def sayHello(name,age):
 print(f'Hello {name} Ur age: {age}')

#position argument
sayHello('Mishan', 21)
sayHello('Regmi', 22)

#keyword argument
sayHello(age = 55, name = 'Master')

#default parameter
def sayHello(name = 'Yodha',age = 25):
 print(f'Hello {name} Ur age: {age}')

sayHello()
sayHello("Mishan")