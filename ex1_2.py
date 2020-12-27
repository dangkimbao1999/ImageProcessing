import sys
from PIL import Image, ImageDraw
import sys
import math

img = Image.new("RGB", (64,64),"white")
width, height = img.size
c=[32,32]

d = 16
change = int(256/d);

# cityblock
##for x in range(height):
##    for y in range(width):
##        if(abs(c[0]-x)+abs(c[1]-y) <= d):
##            proportion = abs(abs(c[0]-x)+abs(c[1]-y) - d)
##            img.putpixel((x,y),(change*proportion,change*proportion,change*proportion,0))

# euclide
##for x in range(height):
##    for y in range(width):
##        if(round(math.sqrt(pow(c[0]-x,2) + pow(c[1]-y,2)))<=d):
##            proportion = abs(round(math.sqrt(pow(c[0]-x,2) + pow(c[1]-y,2))) - d)
##            img.putpixel((x,y),(change*proportion,change*proportion,change*proportion,0))
##            
# cityblock
for x in range(height):
    for y in range(width):
        if(round(max(abs(c[0]-x),abs(c[1]-y)))<=d):
            proportion = abs(max(abs(c[0]-x),abs(c[1]-y)) - d)
            img.putpixel((x,y),(change*proportion,change*proportion,change*proportion,0))
#length-code'
def run_length():
    inValue = 0;
    arr = []
    for x in range(height):
        for y in range(width):
            r,g,b = img.getpixel((x,y))
            if( r == g == b == 0 and inValue == 0):
                inValue = 1
                startY = y
            elif( r == g == b == 0 and inValue == 1):
                inValue = 0
                endY = y
                print(str(x)+","+str(startY)+","+str(endY))
                arr.append(x)
                arr.append(startY)
                arr.append(endY)
                continue
    return arr
img.show() 
i = 0
arr = run_length();
