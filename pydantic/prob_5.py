from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

data= {"name":"sonu","age":29}
check= User.model_validate(data)
print(check)