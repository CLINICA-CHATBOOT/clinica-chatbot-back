from pydantic import BaseModel

class Message(BaseModel):
    content: str

class ResponseMessage(BaseModel):
    response: str
