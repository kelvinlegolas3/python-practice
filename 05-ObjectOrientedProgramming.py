# Assessment 5  : Object Oriented Programming
# Link          : https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/02-Object%20Oriented%20Programming%20Homework.ipynb

# 1.
print("Exercise # 1:")


from math import sqrt

class Line():
    
    def __init__(self, coor1, coor2):
        self.x2, self.x1 = coor2[0], coor1[0]
        self.y2, self.y1 = coor2[1], coor1[1]
        
    def distance(self):
        print(sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2))
        
    def slope(self):
        print((self.y2 - self.y1) / (self.x2 - self.x1))


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