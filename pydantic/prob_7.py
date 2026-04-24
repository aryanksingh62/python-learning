from pydantic import BaseModel, field_validator
from typing import Optional

class Employee(BaseModel):
    name: str
    salary: int
    department: Optional[str]="General"

    @field_validator("salary")
    def salary_range(cls,salary):
        if salary<10000:
            raise ValueError("Salary is less then 10,000")
        return salary
    
    @field_validator("name")
    def name_not_empty(cls, name):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        return name
    
data={"name":"shubham","salary":23000,"department":"Maths"}
result= Employee(**data)
print(result)