from pydantic import BaseModel, Field
from typing import List

class SupportAdmiralOutput(BaseModel):
    response: str = Field(description="The query to ask from the vector database or final anwer to the user")
    