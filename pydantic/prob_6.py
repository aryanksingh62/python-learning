from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

json_data='{"name": "Rahul", "age": 22}'
parse_data= User.model_validate_json(json_data)

final_data =parse_data.model_dump_json()
print(final_data)