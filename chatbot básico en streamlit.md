# Chatbot de Sistemas Embebidos

## Descripción
Este proyecto consiste en el desarrollo de un chatbot básico utilizando Streamlit, orientado a responder preguntas sobre sistemas embebidos como microcontroladores, sensores, Arduino e IoT.

---

## Instalación

###  Evidencia instalación de Streamlit

<img width="1365" height="372" alt="1" src="https://github.com/user-attachments/assets/9755f022-4b06-49a5-a621-fdf78b71950a" />


Comando utilizado:

"pip install streamlit"


---

## Ubicación del proyecto

### Evidencia de la carpeta donde se guardó el archivo

<img width="747" height="148" alt="2" src="https://github.com/user-attachments/assets/9f730433-7d6f-4fad-acf7-99f9a720b187" />


Ruta del archivo:
C:\Users\Paula\OneDrive\Documentos


---

## Ejecución del chatbot

###  Evidencia de ejecución en terminal

<img width="635" height="154" alt="3" src="https://github.com/user-attachments/assets/45765739-dc43-4f24-97a2-cda2d46e3f28" />


Comando utilizado:

streamlit run app.py


---

##  Resultado en navegador

###  Evidencia del chatbot funcionando

<img width="1365" height="680" alt="4" src="https://github.com/user-attachments/assets/4371dc0e-555f-4281-b7a2-ad0bcbab1bed" />


##  Código fuente

import streamlit as st

st.set_page_config(page_title="Chatbot Sistemas Embebidos")

st.title(" Chatbot de Sistemas Embebidos")

# Historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Entrada del usuario
user_input = st.chat_input("Haz una pregunta sobre sistemas embebidos...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Respuestas
    if "microcontrolador" in user_input.lower():
        response = "Un microcontrolador es un circuito integrado que contiene CPU, memoria y periféricos."
    
    elif "arduino" in user_input.lower():
        response = "Arduino es una plataforma de hardware libre utilizada para sistemas embebidos."
    
    elif "raspberry" in user_input.lower():
        response = "Raspberry Pi es una mini computadora usada en IoT y sistemas embebidos."
    
    elif "sensor" in user_input.lower():
        response = "Los sensores permiten captar información del entorno como temperatura, luz o movimiento."
    
    elif "iot" in user_input.lower():
        response = "IoT conecta dispositivos embebidos a internet para intercambio de datos."
    
    else:
        response = "Pregúntame sobre Arduino, sensores, IoT o microcontroladores."

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

## Despliegue en la nube

Aplicación desplegada en Streamlit Cloud.

- Link del chatbot:

http://localhost:8501/

Conclusiones
Se logró implementar un chatbot funcional utilizando Streamlit.
Se comprendió el uso de interfaces interactivas en Python.
Se aplicaron conceptos básicos de sistemas embebidos.
El sistema puede escalarse a inteligencia artificial.
