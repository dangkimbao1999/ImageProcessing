from PIL import Image, ImageFilter
from numpy import *
import math

image = Image.open("D:/studies/word_image_generator-master/Chest_HoanMy_98.jpg")
image = image.resize((256,256))
image = image.convert("L")
##image = image.filter(ImageFilter.FIND_EDGES)
##image = image.filter(ImageFilter.Kernel((3,3),(1,2,1,0,0,0,-1,-2,-1),1,0))
image.load()
h1 = array([[-1,0,1],[-2,0,2],[-1,0,1]])
h2 = array([[1,2,1],[0,0,0],[-1,-2,-1]])
h = sqrt(h1**2+h2**2)
height=image.size[0]
width=image.size[1]

img_x = Image.new("L",(256,256),"white")

for y in range(1,255):
    for x in range(1,255):
        value = image.getpixel((x-1,y-1))*h1[0][0] + image.getpixel((x,y-1))*h1[0][1] + image.getpixel((x+1,y-1))*h1[0][2] +\
                image.getpixel((x-1,y))*h1[1][0] + image.getpixel((x,y))*h1[1][1] + image.getpixel((x+1,y))*h1[1][2]+\
                image.getpixel((x-1,y+1))*h1[2][0] + image.getpixel((x,y+1))*h1[2][1] + image.getpixel((x+1,y+1))*h1[2][2]
        value = int(value)
        #print(value)
        img_x.putpixel((x,y),value)
img_x.show()

img_y = Image.new("L",(256,256),"white")
for y in range(1,255):
    for x in range(1,255):
        value = image.getpixel((x-1,y-1))*h2[0][0] + image.getpixel((x,y-1))*h2[0][1] + image.getpixel((x+1,y-1))*h2[0][2] +\
                image.getpixel((x-1,y))*h2[1][0] + image.getpixel((x,y))*h2[1][1] + image.getpixel((x+1,y))*h2[1][2]+\
                image.getpixel((x-1,y+1))*h2[2][0] + image.getpixel((x,y+1))*h2[2][1] + image.getpixel((x+1,y+1))*h2[2][2]
        value = int(value)
        #print(value)
        img_y.putpixel((x,y),value)
img_y.show()
img = Image.new("L",(256,256),"white")
for y in range(1,255):
    for x in range(1,255):
        value = sqrt(img_x.getpixel((x,y))**2 + img_y.getpixel((x,y)))
        value = int(value)
        #print(value)
        img.putpixel((x,y),value)
img.show()