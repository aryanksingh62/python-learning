from pydantic import BaseModel,Field
from typing import List 

class AgentResponse(BaseModel):
    summary: str
    key_points: List[str]
    confidence_score: float = Field(ge=0,lt=1)
    action_items: List[str]

data = {
    "summary": "The company's Q3 performance was strong overall.",
    "key_points": [
        "Revenue increased by 23%",
        "Customer retention improved",
        "New product launch successful"
    ],
    "confidence_score": 0.85,
    "action_items": [
        "Schedule follow-up meeting",
        "Prepare Q4 forecast",
        "Send report to stakeholders"
    ]
}
result= AgentResponse.model_validate(data)
print(result)