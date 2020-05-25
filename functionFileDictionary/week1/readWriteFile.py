#creating the file if not exist and writing inside the file

f= open("test.txt","w+")

for number in range(13):
    square = number * number
    '''
    f.write(str(square))
    f.write("\n")
    '''
    # or

    f.write(str(square) + '\n')
f.close()

#now reading from that same file
new_file = open("test.txt", "r")

#print(new_file.read(10))
print(new_file.read()[:10])

#using with for files
with open('test.txt', 'r') as re:
    for line in re:
        print(line)

#being more general with with
'''
file = test.txt
with open(file, 'r') as re:
    re.read()
    re.readline()
    re.readlines()
    for line in re:
        do something with each line

WE CAN DO THI WITH WRITE ALSO
'''