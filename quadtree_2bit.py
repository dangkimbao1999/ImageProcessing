
from PIL import Image 
import math
s=""
class Point(object): # at a pixel
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
class Pixel(object):
    def __init__(self, color = 0,topLeft = Point(0, 0),bottomRight = Point(0, 0),neighbor =[0,0]):
        self.color = color
        self.topLeft = topLeft
        self.bottomRight = bottomRight
        self.neighbor = neighbor
class quadtree(): 
    def __init__(self, image): 
        self.level = 0
        # Total number of nodes of tree 
        self.size = 0
  
        # Store image pixelmap 
        self.image = image.load() 
  
        # Array of nodes 
        self.tree = [] 
        self.x = image.size[0] #width 
        self.y = image.size[1] #height
  
        size = image.size[0] * image.size[1] 
        level = 0
        # Count number of nodes and level 
        while(size >= 1): 
            self.size += size 
            size /= 4
            self.level = level
            level +=1
        print("number of nodes '{0}' and number of level '{1}'" .format(self.size,level))
        size = image.size[0] * image.size[1] 
        print("total pixel %d" %size)
        # Initialize array elements 
        for i in range(0, int(self.size)): 
            self.tree.append(Pixel()) 

        
        # Store leaves into array 
        count = 0
        for i in range(image.size[0] - 1, 0, -2): 
            for j in range(image.size[1] - 1, 0, -2): 
                # pixel at i,j (bottom right)
                # every leaf store whole it's color value
                self.tree[int(self.size) - 1 - 4 * count] = Pixel(self.image[i, j],  
                        Point(i, j),  
                        Point(i, j)) 
                self.tree[int(self.size)- 2 - 4 * count] = Pixel(self.image[i, j - 1],  
                        Point(i, j - 1), 
                        Point(i, j - 1)) 
                self.tree[int(self.size) - 3 - 4 * count] = Pixel(self.image[i - 1, j],  
                        Point(i - 1, j),  
                        Point(i - 1, j)) 
                self.tree[int(self.size) - 4 - 4 * count] = Pixel(self.image[i - 1, j - 1],  
                        Point(i - 1, j - 1),  
                        Point(i - 1, j - 1))
                count += 1
        # Calculate and create parent nodes by taking average value
        print("parent start: %d" %count)
        end_leaf = int(self.size) - 4 * count - 1
        for i in range(end_leaf, -1, -1):
            # chứa 4 pixel trong 1 leaf đó cộng lại
            
            self.tree[i] = Pixel( (self.tree[4*i+1].color + self.tree[4*i+2].color + self.tree[4*i+3].color + self.tree[4*i+4].color) /4,
                  self.tree[4 * i + 1].topLeft,
                  self.tree[4 * i + 4].bottomRight,[4*i+1,4*i+4])
##              # position of pixel đầu và cuối trong cụm 4 pixel trong 1 leaf
                #DFS, những node cuối trong array là leaves, mấy node đầu là hợp của 4 node kề nhau
                #vd 8*8 = 64 => 85 node kể cả parent lần leaves-> 21 node parent và 64 leaves
            print("{0} includes node: {1} to {2}, value: {3}".format(i,4*i+1,4*i+4,self.tree[i].color))
                
    def print(self,v):
        visited = set()        
        global s
        self.printUtil(v,visited)
        #print(s)
        print(self.level)
        while(self.level >= 0):
            m=0
            finalStr=""
            while(m < len(s)):
                if s[m] == "g" and s[m+2]=="w" and s[m+3]=="w" and s[m+4]=="w" and s[m+5]=="w":
                    finalStr += "w"
                    m+=6
                elif s[m] == "g" and s[m+2]=="b" and s[m+3]=="b" and s[m+4]=="b" and s[m+5]=="b":
                    finalStr +="b"
                    m+=6
                else:
                    finalStr+=s[m]
                m+=1
            self.level -=1
            s = finalStr
        print(self.level)
        print(finalStr)
    def printUtil(self,v,visited):
        global s
        visited.add(v)
        current  = self.tree[v]
        if v < self.size - self.x * self.y:
            s+="g("
            
        else:
            if self.tree[v].color == 255:
                s+="w"
               
            elif self.tree[v].color == 0:
                s+="b"

        for neighbour in range(self.tree[v].neighbor[0],self.tree[v].neighbor[1]+1):
            if neighbour not in visited:
                self.printUtil(neighbour,visited)
        if( v < self.size -self.x * self.y):
            s+=")"



    def disp(self):
        for i in range(0,85):
            print("{0} and {1}".format(self.tree[i].neighbor[0],self.tree[i].neighbor[1]))

img = Image.open('Chest_HoanMy_98.jpg').resize((128,128)).convert('1')
img.show()

quadTree = quadtree(img)
quadTree.print(0)
