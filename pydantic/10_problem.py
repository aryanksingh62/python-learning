from pydantic import BaseModel, EmailStr,Field,ValidationError,field_validator
import json
from pathlib import Path

def read_file(input_file):
    with open(input_file,"r") as f:
        data= json.load(f)
        if data:
            return data
        else:
            print(f"input file {input_file} is empty")
            return
    
def save_to_json(output_file,new_data):
    if not new_data:
        print("there is no valid data to saved")
        return
    with open(output_file,"w") as f:
        json.dump(new_data,f,indent=2)
        print("✅valid data daved succesfully")

class CheckData(BaseModel):
    name: str
    age: int= Field(ge=0)
    email: EmailStr

    @field_validator("name")
    def name_not_empty(cls,nam):
        if not nam or not nam.strip():
            raise ValueError("name is empty")
        return nam

if __name__=="__main__":
    INPUT_FILE= "user.json"
    OUTPUT_FILE= "valid.json"

    if not Path(INPUT_FILE).is_file():
        print("Invalid File")
    else:
        new_data=[]
        data= read_file(INPUT_FILE)
        if data:
            for i in data:
                try:
                    result= CheckData.model_validate(i)
                    new_data.append(i)
                except ValidationError as e:
                    pass
        
        save_to_json(OUTPUT_FILE,new_data)