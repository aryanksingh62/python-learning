from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    country: str

class Person(BaseModel):
    name: str
    age: int
    address: Address

details={"name":"sonu","age":23,
         "address":{"street":"borivali","city":"mumbai","country":"india"}}

d1= Person(**details)
print(d1)
print(d1.address.city)