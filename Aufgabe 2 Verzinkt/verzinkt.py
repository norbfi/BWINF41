from PIL import Image, ImageDraw
import random 
import time 

#bild erzeugen
width, height = 100, 100
img = Image.new("RGB", (100, 100), "black")

#variables for color 
right = (185, 171, 171)
left = (185, 171, 171)
top = (132, 125, 125)
bottom = (213, 211, 211)

#random spawnpoint
def spwnpnt():
    spwnpnt = (random.randint(0,100),random.randint(0,100))
    return spwnpnt 

#simulation code
def crisgrow(spwnpnt):
    spwnpnt = spwnpnt()

    for i in range(spwnpnt[0], 100):
        for j in range(spwnpnt[1], 100):
            img.putpixel((i, j), bottom)
            


#for i in range(0,50):
 #   for j in range(0,50):
  #      img.putpixel((i, j), bottom)

crisgrow(spwnpnt)


img.save("img.png")

#TODO farb algorithmus