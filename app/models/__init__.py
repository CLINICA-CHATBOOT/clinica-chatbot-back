from datetime import datetime
from pydantic import BaseModel

class Message(BaseModel):
    professional: str
    patient_name: str
    appointment_date: datetime

class ResponseMessage(BaseModel):
    reply: str