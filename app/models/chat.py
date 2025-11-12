from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    content: str

class ResponseMessage(BaseModel):
    response: str

class Appointment(BaseModel):
    professional: str
    patient_name: str
    date: datetime