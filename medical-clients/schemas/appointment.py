from pydantic import BaseModel
from typing import Optional

class Appointment(BaseModel):
    id: Optional[int]
    userid: Optional[int]
    name: Optional[str]
    specialty: str
    subject: str
    date: str