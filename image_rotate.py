from PIL import Image
import math

image = Image.open("Chest_HoanMy_98.jpg")
image = image.resize((256,256))
image = image.convert("L")
angle=45

angle*=-1
angle=math.radians(angle)
cosine=math.cos(angle)
sine=math.sin(angle)
height=image.size[0]                                   
width=image.size[1]                                    

new_height  = round(abs(image.size[0]*cosine)+abs(image.size[1]*sine))+1
new_width  = round(abs(image.size[1]*cosine)+abs(image.size[0]*sine))+1

nearest = Image.new("L",(256 ,256),"white")
interpolation = Image.new("L",(256,256),"white")

for y in range(height):
    for x in range(width):
       
        #nearest
        origin_y= round(-x*sine+y*cosine)
        origin_x= round(x*cosine+y*sine)
        if(0<=origin_x<width and 0 <= origin_y < height ):
            value = image.getpixel((origin_x,origin_y))
            nearest.putpixel((x,y), value)

        #value interpolation
        origin_x= -x*sine+y*cosine
        origin_y= x*cosine+y*sine
        k = int(origin_x)
        l = int(origin_y)
        a = origin_x - k;
        b = origin_y - l;

        if( 0<=l<width-1 and 0 <= k <height-1):
            value = a*b*image.getpixel((l,k)) + (1-a)*b*image.getpixel((l+1,k)) +\
                    (1-b)*a*image.getpixel((l,k+1)) +\
                    (1-a)*(1-b)*image.getpixel((l+1,k+1)) 
            interpolation.putpixel((x,y),int(value))
        #print(value)
nearest.show()
interpolation.show()
        
        
        
