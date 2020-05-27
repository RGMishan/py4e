#accumulating in dictionary

f = open('myDict.txt', 'r')
txt = f.read()
x = {} #initialize a empty dictionary

for c in txt:
    if c not in x:
        x[c] = 0 #character not seen so initialized as zero
    x[c] = x[c] + 1 # not seen so increment in counter

print('The no of m in file is', str(x['m']) ,"times.") #passing m in the c value
print('The no of m in file is', str(x['a']) ,"times.")

for c in x.keys():
    print("letter",c, "occur", str(x[c]), "times")