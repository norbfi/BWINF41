from PIL import Image, ImageDraw



width, height = 100, 100
weiss = (255, 255, 255) 


img = Image.new("RGB", (100, 100), "black")

img.putpixel((1,1), weiss)

img.save("img.png")


#TODO farb algorithmus 