#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for image in picture: # Going through the list value
  for pixel in image: # Going through the list's list value
    if (pixel == 1): # Checking if value is 1 or not
      print('*', end ="") #if it is one the print a * and dont go to next line
    else:
      print(' ', end ="") # if it is not one print empty space and dont go to next line
  print('') # When we come out of the second loop once and get to next list item, 
            #then more to next line as print change line