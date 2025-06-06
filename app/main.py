from fastapi import FastAPI
from pydantic import BaseModel
from app.model import clasificar_mensaje

app = FastAPI()

class MensajeEntrada(BaseModel):
    mensaje: str

@app.post("/clasificar")
def clasificar_texto(entrada: MensajeEntrada):
    resultado = clasificar_mensaje(entrada.mensaje)
    return resultado
