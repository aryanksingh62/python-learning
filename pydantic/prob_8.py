from pydantic import BaseModel,field_validator
from typing import List

class Student(BaseModel):
    name:str
    grade: str

class Classroom(BaseModel):
    teacher: str
    students: List[Student]

    @field_validator("students")
    def students_not_empty(cls,list_std):
        if not list_std:
            raise ValueError("there is no studnets in the classroom")
        return list_std
    
data = {
    "teacher": "Mr. Sharma",
    "students": [
        {"name": "Rahul", "grade": "A"},
        {"name": "Priya", "grade": "B"},
        {"name": "Amit", "grade": "A+"}
    ]
}
result= Classroom.model_validate(data)
print(result)