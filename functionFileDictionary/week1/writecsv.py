olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

header = 'Name,          Age,         Sports'
print(header)
for olymp in olympians:
    row = "{},   {},   {}".format(olymp[0],olymp[1],olymp[2])
    print(row)

#Now we are storing this in the CSV file

outfile = open("olympicsDetails.csv", "w+")
outfile.write('Name,  Age,  Sports')
outfile.write('\n')
for olymp in olympians:
    #1  row = ",".join(olymp) # we can use this if our data was string as age is an interger value

    row = ",".join([olymp[0],str(olymp[1]),olymp[2]]) #Join takes only one argument
    #Join takes only string and and one value is interger i.e age  OR   WE CAN DEFINE IT AS STRING ABOVE
    #Join doesn't let us format as the next line of code does

    #     OR WE CAN ALSO DO
    #2  row = "{} , {} , {}".format(olymp[0],olymp[1],olymp[2])

    #3  row = olymp[0] + ',' + str(olymp[1]) + ',' + olymp[2]

    outfile.write(row)
    outfile.write('\n')
outfile.close()
