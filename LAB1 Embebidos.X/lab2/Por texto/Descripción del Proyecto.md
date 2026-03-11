#  Arduino Chatbot: Control de Iluminación y Temperatura

##  Descripción del Proyecto

Este proyecto implementa un sistema sencillo de **control de iluminación y monitoreo de temperatura utilizando Arduino y Python**.  

El sistema permite que un usuario interactúe con un **chatbot**, el cual envía comandos al Arduino mediante **comunicación serial**.

El Arduino controla **dos LEDs (rojo y verde)** y mide la **temperatura usando un sensor DHT11**.

El proyecto se implementó en dos formas de interacción:

-  Chatbot por texto
-  Chatbot por voz

---

# Hardware Utilizado

- Arduino UNO
- Sensor de temperatura **DHT11**
- 2 LEDs (Rojo y Verde)
- Resistencias 220Ω o 330Ω
- Protoboard
- Cables de conexión
- Computador con Python

---

# Chatbot por Texto

## Descripción

En esta versión se desarrolló un **chatbot básico en Python** que permite al usuario escribir comandos en la terminal para controlar el sistema conectado al Arduino.

El chatbot utiliza la librería **pyserial** para comunicarse con el Arduino a través del puerto serial.

---

## Funcionamiento del Sistema

El flujo del sistema es el siguiente:

1. El usuario escribe un comando en la terminal.
2. El programa en Python interpreta el texto ingresado.
3. Python envía un comando al Arduino mediante **comunicación serial**.
4. Arduino recibe el comando y ejecuta la acción correspondiente.
5. Arduino envía una respuesta al programa.
6. El chatbot muestra la respuesta al usuario.

---

## Ejemplo de interacción

```
Chatbot iniciado

Tu: rojo encender
Arduino: LED rojo encendido

Tu: verde encender
Arduino: LED verde encendido

Tu: temperatura
Arduino: Temperatura: 25 C

Tu: rojo apagar
Arduino: LED rojo apagado
```

---

## Comandos disponibles

```
rojo encender
rojo apagar
verde encender
verde apagar
temperatura
```
