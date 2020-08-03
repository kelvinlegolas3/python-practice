# Assessment 5  : Object Oriented Programming
# Link          : https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/02-Object%20Oriented%20Programming%20Homework.ipynb

# 1.
print("Exercise # 1:")


from math import sqrt

class Line():
    
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        
        print(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        
        print((y2 - y1) / (x2 - x1))


coordinate1 = (3, 2)
coordinate2 = (8, 10)

line = Line(coordinate1, coordinate2)
line.distance()
line.slope()


# 2.
print("Exercise # 2:")

from math import pi

class Cylinder():
    
    def __init__(self, height=1, radius=1):
        self.h, self.r = height, radius
    
    def volume(self):
        print(pi * self.r ** 2 * self.h)
    
    def surface_area(self):
        print(2 * pi * self.r * self.h + 2 * pi * self.r ** 2)
    
cylinder = Cylinder(2, 3)
cylinder.volume()
cylinder.surface_area()