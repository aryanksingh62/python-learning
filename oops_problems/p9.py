from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self,):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius**2
    
    def perimeter(self):
        return 2*3.14*self.radius

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)

c = Circle(5)
print(c.area())         
print(c.perimeter())


r = Rectangle(4, 6)
print(r.area())      
print(r.perimeter())  


try:
    s = Shape() 
except TypeError as e:
    print(e)   

# Test isinstance
print(isinstance(c, Shape))   # True
print(isinstance(r, Shape))   # True