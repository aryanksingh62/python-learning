from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

data= {"name":"aryan","age":13,"email":"aryan@.com"}

user= User(**data)
print(user)