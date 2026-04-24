from pydantic import BaseModel
from typing import Optional

class Profile(BaseModel):
    username: str
    bio: Optional[str] = None
    followers: int =0
    verified: bool = False

pro_data= {"username":"sasxena","bio":"fan of marvel",
           "followers":23,"verified":True}

p1= Profile(**pro_data)
print(p1)