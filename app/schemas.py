from pydantic import BaseModel

class MessageRequest(BaseModel):
    mensaje: str

class MessageResponse(BaseModel):
    categoria: str
    detalle: str
