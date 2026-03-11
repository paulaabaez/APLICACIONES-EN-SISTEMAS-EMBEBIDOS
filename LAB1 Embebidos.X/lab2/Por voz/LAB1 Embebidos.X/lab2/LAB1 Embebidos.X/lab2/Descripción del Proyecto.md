# Arduino Chatbot: Control de Iluminación y Temperatura

## Descripción del Proyecto
# Chatbot por Voz

## Descripción

En esta versión del sistema se implementó **control por voz**, permitiendo al usuario interactuar con el Arduino utilizando el micrófono del computador.

Se utilizaron librerías de Python para reconocer comandos hablados y convertirlos en instrucciones que el Arduino puede interpretar.

Además, el sistema puede **responder con voz** al usuario.

---

## Funcionamiento del Sistema

1. El programa activa el micrófono del computador.
2. El usuario dice un comando de voz.
3. La librería de reconocimiento de voz convierte el audio en texto.
4. Python interpreta el comando reconocido.
5. El comando se envía al Arduino mediante comunicación serial.
6. Arduino ejecuta la acción solicitada.
7. Arduino envía una respuesta.
8. El chatbot muestra la respuesta y la reproduce mediante voz.

---

## Librerías utilizadas

Las siguientes librerías fueron utilizadas para implementar el reconocimiento de voz:

```
SpeechRecognition
pyttsx3
pyaudio
pyserial
```

Instalación de dependencias:

```
pip install pyserial
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
```

---

## Ejemplo de interacción por voz

Usuario dice:

```
rojo encender
```

Respuesta del sistema:

```
Arduino: LED rojo encendido
```

Usuario dice:

```
temperatura
```

Respuesta:

```
Arduino: Temperatura: 24 C
```

---

# Arquitectura del Sistema

```
Usuario
   │
   ▼
Chatbot Python (Texto o Voz)
   │
   ▼
Comunicación Serial
   │
   ▼
Arduino
   │
   ├── Control de LEDs
   └── Sensor de Temperatura DHT11
```

---

# Tecnologías Utilizadas

- Arduino
- Python 3
- Comunicación Serial
- Speech Recognition
- Sistemas Embebidos

---

# Conclusión

Este proyecto demuestra la integración entre **software y hardware**, permitiendo controlar dispositivos físicos mediante **chatbots en Python**.

La implementación del control por voz muestra cómo tecnologías de **reconocimiento de voz** pueden aplicarse en sistemas embebidos para crear interfaces más naturales e intuitivas.

---

# Autor

Proyecto desarrollado como práctica de **Sistemas Embebidos** utilizando Arduino y Python.
