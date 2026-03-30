class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "poo-poo"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f"{self.name} says Woof"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f"{self.name} says Meow"

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
       return f"{self.name} says Moo"

def make_sounds(animals):
    for animal in animals:
        print(animal.speak())

d = Dog("Rocky")
c = Cat("Whiskers")
cow = Cow("Bessie")

animals = [d, c, cow]
make_sounds(animals)