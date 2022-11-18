from PIL import Image, ImageDraw
import random 
import time 

#bild erzeugen
img = Image.new("RGB", (101, 101), "black")

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
    
    img.putpixel(spwnpnt, (100,0,0))
    for x in range(spwnpnt[0]):
        for y in range(spwnpnt[1]):

            if img.getpixel((x + 1, y)) == (0,0,0):
                img.putpixel((x + 1, y), left)
            else:
                break

            y = y+1
        x = x+1
            


#for i in range(0,50):
 #   for j in range(0,50):
  #      img.putpixel((i, j), bottom)


crisgrow(spwnpnt)
crisgrow(spwnpnt)


img.save("img.png")

#TODO farb algorithmus


#test