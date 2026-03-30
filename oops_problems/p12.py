class Flyable:
    def fly(self):
        return f"{self.name} can fly"
    
class Swimable:
    def swim(self):
        return f"{self.name} can swim"
    
class Duck(Flyable,Swimable):
    def __init__(self,name,species):
        self.name=name
        self.species=species

d = Duck("Donald", "Mallard")

print(d.fly())
print(d.swim())     

# Test multiple inheritance
print(isinstance(d, Flyable)) 
print(isinstance(d, Swimable))

# See both parents
print(Duck.__bases__)  