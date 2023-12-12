class Shape:
    
    def colour(self, colour):
        self.colour = colour
      
class Rectangle(Shape):
    
    def __init__(self, l, b):
        self.l = l
        self.b = b
        
    def calc_area(self):
        return self.l * self.b, self.colour
        
class Triangle(Shape):
    
    def __init__(self, b, h):
        self.b = b
        self.h = h
        
    def calc_area(self):
        return 0.5 * self.b * self.h, self.colour
    
l = int(input("Enter length of Rectangle: "))
b = int(input("Enter breadth of Rectangle: "))    
Rect = Rectangle(l, b)
Rect.colour = input("Enter colour of Rectangle: ")
print(Rect.calc_area())

b = int(input("Enter base of Triangle: "))
h = int(input("Enter height of Triangle: "))
Tri = Triangle(b, h)
Tri.colour = input("Enter colour of Triangle: ")
print(Tri.calc_area())