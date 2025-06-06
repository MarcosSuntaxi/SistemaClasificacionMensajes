import streamlit as st
import requests

st.title("Clasificador de Mensajes")
st.write("Ingrese un mensaje para clasificarlo como Urgente, Normal o Moderado.")

mensaje = st.text_area("Mensaje")

if st.button("Clasificar"):
    if mensaje.strip() == "":
        st.warning("Por favor ingrese un mensaje.")
    else:
        try:
            respuesta = requests.post(
                "http://127.0.0.1:8000/clasificar",
                json={"mensaje": mensaje}
            )
            if respuesta.status_code == 200:
                resultado = respuesta.json()
                st.success(f"**Etiqueta clasificada:** {resultado['clasificacion']}")

                st.subheader("Puntajes por categoría:")
                for etiqueta, score in resultado["puntajes"].items():
                    st.write(f"- **{etiqueta}**: {score:.2f}")
            else:
                st.error("Error al clasificar el mensaje. Código de estado: " + str(respuesta.status_code))
        except Exception as e:
            st.error(f"No se pudo conectar con el servidor: {e}")
