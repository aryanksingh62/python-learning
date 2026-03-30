class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, other):
        return Vector(self.i+other.i, self.j+other.j , self.k+other.k)
    
    def __sub__(self,other):
        return Vector(self.i-other.i, self.j-other.j,  self.k-other.k)
    
    def __eq__(self,other):
        return self.i==other.i and self.j==other.j and self.k==other.k
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(1, 2, 3)

print(v1)

print(v1 + v2) 

print(v2 - v1)

print(v1 == v3)
print(v1 == v2)


v4 = v1 + v2
print(v4.i)
print(v4.j)
print(v4.k) 