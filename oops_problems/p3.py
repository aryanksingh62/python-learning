class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,lenght,width):
        super().__init__()
        self.length=lenght
        self.width=width
    def area(self):
        return self.length*self.width
class Triangle(Shape):
    def __init__(self,base,height):
        super().__init__()
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
c = Circle(5)
print(c.area()) 

# Test Rectangle
r = Rectangle(4, 6)
print(r.area()) 

# Test Triangle
t = Triangle(10, 8)
print(t.area())    

# Test override — parent vs child
s = Shape()
print(s.area())       
print(c.area())     

# Test inheritance
print(isinstance(c, Shape)) 
print(isinstance(r, Shape))   
print(isinstance(t, Shape)) 