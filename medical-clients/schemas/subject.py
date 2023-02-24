from pydantic import BaseModel
from typing import Optional

class Subject(BaseModel):
    id: Optional[int]
    subject: str
    specialty: str