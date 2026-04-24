from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)

p1 = Product(name="Laptop", price=55000, quantity=2)
print(p1)
#to check the pydantic error
p2 = Product(name="Laptop", price=55000, quantity=-1) 
print(p2)