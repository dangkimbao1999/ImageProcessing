from __future__ import print_function
import sys
from PIL import Image, ImageDraw
import sys
import math

img = Image.new("L", (64,64),"white")
width, height = img.size
center = sys.argv[0];
c=[32,32]
d = 10

# for euclide: 1 region
##for x in range(height):
##    for y in range(width):
##       if(round(math.sqrt(pow(c[0]-x,2) + pow(c[1]-y,2)))==d):
##           img.putpixel((x,y),1)
##

# cityblock: 1 region
##for x in range(height):
##    for y in range(width):
##        if(abs(c[0]-x)+abs(c[1]-y) == d):
##            img.putpixel((x,y),1)

# chessboard: 1 region
for x in range(height):
    for y in range(width):
        if(max(abs(c[0]-x),abs(c[1]-y)) == d):
            img.putpixel((x,y),1)


        
img.show()
