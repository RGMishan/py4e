fileconnection = open('grades.txt', 'r')
lines = fileconnection.readlines()
for lin in lines[0:]:
    print(lin.strip())
print("------------------")
header = lines[0]
field_name = header.strip().split(',')
print(field_name)

for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[2] != '':
       print("{}:    {};     {}".format(vals[0],vals[1],vals[2]))

