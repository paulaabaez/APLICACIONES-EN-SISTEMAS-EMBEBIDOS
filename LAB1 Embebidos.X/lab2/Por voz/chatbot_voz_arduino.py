import serial
import time
import speech_recognition as sr
import pyttsx3

arduino = serial.Serial('COM4',9600)
time.sleep(2)

recognizer = sr.Recognizer()

engine = pyttsx3.init()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

print("Chatbot por voz iniciado")

while True:

    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        mensaje = recognizer.recognize_google(audio, language="es-ES")
        mensaje = mensaje.lower()

        print("Tu dijiste:", mensaje)

        if "rojo encender" in mensaje:
            arduino.write(b"LED ROJO ON\n")

        elif "rojo apagar" in mensaje:
            arduino.write(b"LED ROJO OFF\n")

        elif "verde encender" in mensaje:
            arduino.write(b"LED VERDE ON\n")

        elif "verde apagar" in mensaje:
            arduino.write(b"LED VERDE OFF\n")

        elif "temperatura" in mensaje:
            arduino.write(b"TEMPERATURA\n")

        else:
            hablar("No entendí el comando")
            continue

        time.sleep(1)

        respuesta = arduino.readline().decode().strip()

        print("Arduino:",respuesta)

        hablar(respuesta)

    except:
        print("No entendí")