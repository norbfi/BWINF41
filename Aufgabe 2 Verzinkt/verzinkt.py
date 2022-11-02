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

startpoint = (50,50)

#simulation code


#for i in range(0,50):
 #   for j in range(0,50):
  #      img.putpixel((i, j), bottom)



img.save("img.png")


#TODO farb algorithmus