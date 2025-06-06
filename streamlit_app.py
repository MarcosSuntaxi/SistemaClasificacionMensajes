import streamlit as st
import requests

# Configuración de la página
st.set_page_config(
    page_title="Clasificador de Mensajes",
    page_icon="🧠",
    layout="centered"
)

# Título e instrucciones
st.title("🧠 Clasificador de Mensajes con IA")
st.markdown("""
Esta herramienta utiliza **inteligencia artificial (IA)** para clasificar mensajes de texto según su nivel de urgencia.

Las posibles categorías son:
- 🔴 **Urgente**
- 🟡 **Moderado**
- 🟢 **Normal**

Es ideal para sistemas de soporte, filtrado de mensajes o análisis automático de prioridades.
""")

# Entrada de mensaje
st.subheader("✉️ Ingrese su mensaje:")
mensaje = st.text_area("Texto del mensaje", height=150, placeholder="Ejemplo: Necesito ayuda urgente, el sistema está caído.")

# Botones de acción
col1, col2 = st.columns([1, 1])
with col1:
    clasificar = st.button("Clasificar")
with col2:
    limpiar = st.button("Limpiar")

# Limpiar mensaje
if limpiar:
    st.experimental_rerun()

# Clasificación del mensaje
if clasificar:
    if mensaje.strip() == "":
        st.warning("⚠️ Por favor, ingrese un mensaje antes de clasificar.")
    else:
        try:
            respuesta = requests.post(
                "http://127.0.0.1:8000/clasificar",
                json={"mensaje": mensaje}
            )
            if respuesta.status_code == 200:
                resultado = respuesta.json()
                st.success(f"✅ **Clasificación:** {resultado['clasificacion']}")

                st.subheader("📊 Puntajes por categoría:")
                st.bar_chart(resultado["puntajes"])

                # Mostrar valores numéricos
                for etiqueta, score in resultado["puntajes"].items():
                    st.write(f"- **{etiqueta}**: {score:.4f}")
            else:
                st.error(f"❌ Error al clasificar el mensaje. Código de estado: {respuesta.status_code}")
        except Exception as e:
            st.error(f"🚫 No se pudo conectar con el servidor: `{e}`")

# Footer
st.markdown("---")
st.caption("Desarrollado con ❤️ usando FastAPI, Transformers y Streamlit")
