# 📬 Clasificador de Mensajes (FastAPI + HuggingFace + Streamlit)

Este proyecto es una aplicación de clasificación de texto que permite determinar si un mensaje ingresado es **Urgente**, **Moderado** o **Normal**, usando un modelo preentrenado de lenguaje natural.  
La solución incluye una **API REST desarrollada en FastAPI** y un **frontend interactivo en Streamlit**.

---

## 🚀 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) – Backend API
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index) – Clasificador de texto
- [Streamlit](https://streamlit.io/) – Interfaz de usuario web
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI

---

## 🧠 Funcionalidad

1. El usuario ingresa un mensaje en una interfaz web.
2. El frontend lo envía al backend (FastAPI).
3. El backend usa un modelo de HuggingFace para clasificar el mensaje como:
   - **Urgente**
   - **Normal**
   - **Moderado**
4. Se muestra la categoría predicha junto con los puntajes por cada etiqueta.


---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/clasificador_mensajes.git
cd clasificador_mensajes
```

### 2. Crear entorno virtual e instalar dependencias
python -m venv venv
venv\Scripts\activate  # En Windows
# source venv/bin/activate  # En Linux/Mac

pip install -r requirements.txt

### 3. Ejecutar el backend (API FastAPI)
```bash
uvicorn app.main:app --reload
```
Accede a la documentación automática de la API en:
👉 http://127.0.0.1:8000/docs

### 4. Ejecutar el frontend (Streamlit)
En otra terminal con el entorno virtual activado:
```bash
streamlit run app.py
