from PIL import Image, ImageFilter
from numpy import *
import math

image = Image.open("Chest_HoanMy_98.jpg")
image = image.resize((256,256))
image = image.convert("L")
##image = image.filter(ImageFilter.FIND_EDGES)
##image = image.filter(ImageFilter.Kernel((3,3),(1,2,1,0,0,0,-1,-2,-1),1,0))
image.load()
image.show()
h1 = array([[1,2,1],[0,0,0],[-1,-2,-1]])
height=image.size[0]                                   
width=image.size[1]

img = Image.new("L",(256,256),"white")

for y in range(1,255):
    for x in range(1,255):
        value = image.getpixel((x-1,y-1))*h1[0][0] + image.getpixel((x,y-1))*h1[0][1] + image.getpixel((x+1,y-1))*h1[0][2] +\
                image.getpixel((x-1,y))*h1[1][0] + image.getpixel((x,y))*h1[1][1] + image.getpixel((x+1,y))*h1[1][2]+\
                image.getpixel((x-1,y+1))*h1[2][0] + image.getpixel((x,y+1))*h1[2][1] + image.getpixel((x+1,y+1))*h1[2][2]
        value = int(value)
        #print(value)
        img.putpixel((x,y),value)
img.show()
        
