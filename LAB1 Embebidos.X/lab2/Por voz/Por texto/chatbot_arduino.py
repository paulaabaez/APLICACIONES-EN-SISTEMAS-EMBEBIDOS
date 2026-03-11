import serial
import time

arduino = serial.Serial('COM4',9600)
time.sleep(2)

print("Chatbot iniciado")

while True:

    mensaje = input("Tu: ").lower()

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
        print("No entiendo ese comando")
        continue

    time.sleep(1)

    respuesta = arduino.readline().decode().strip()
    print("Arduino:",respuesta)