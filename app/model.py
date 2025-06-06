from transformers import pipeline

# Crear el pipeline con el modelo de clasificación Zero-Shot
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Lista de etiquetas para clasificación
etiquetas = ["Urgente", "Normal", "Moderado"]

def clasificar_mensaje(mensaje: str) -> dict:
    resultado = classifier(mensaje, etiquetas)
    return {
        "mensaje": mensaje,
        "clasificacion": resultado["labels"][0],  # La más probable
        "puntajes": dict(zip(resultado["labels"], resultado["scores"]))
    }
