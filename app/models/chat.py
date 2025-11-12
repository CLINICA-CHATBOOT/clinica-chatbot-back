from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    content: str

class ResponseMessage(BaseModel):
    response: str

class Appointment(BaseModel):
    professional_id: int
    patient_name: str
    appointment_date: datetime