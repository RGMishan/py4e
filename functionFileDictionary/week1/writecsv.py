olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

header = 'Name,  Age,  Sports'
print(header)
for olamp in olympians:
    row = "{} , {} , {}".format(olympians[0],olympians[1],olympians[2])
    print(row)

