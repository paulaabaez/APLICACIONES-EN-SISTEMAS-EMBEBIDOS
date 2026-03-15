# Detección de Formas y Colores con Arduino y OpenCV

## Descripción

Este proyecto utiliza visión por computadora para detectar **formas y colores** mediante una cámara web.  
El sistema identifica tres combinaciones específicas:

- Círculo rojo
- Rectángulo verde
- Cuadrado azul

Cuando una de estas combinaciones es detectada, el programa envía una señal por comunicación serial a un Arduino, el cual enciende los LEDs correspondientes.

Si no se detecta ningún objeto válido, todos los LEDs permanecen apagados.

---

## Tecnologías utilizadas

- Python
- OpenCV
- Comunicación serial
- Arduino

---

## Lógica del programa

El sistema funciona siguiendo estos pasos:

1. Captura video desde la cámara web.
2. Convierte la imagen al espacio de color HSV para mejorar la detección de colores.
3. Genera máscaras para los colores rojo, verde y azul.
4. Detecta contornos en cada máscara.
5. Selecciona el contorno más grande para evitar ruido.
6. Calcula la forma del objeto usando:
   - Número de vértices del contorno
   - Relación entre ancho y alto
   - Circularidad
7. Combina **forma + color** para validar el objeto detectado.

Solo se aceptan las siguientes combinaciones:

| Forma | Color |
|------|------|
| Círculo | Rojo |
| Rectángulo | Verde |
| Cuadrado | Azul |

---

## Comunicación con Arduino

El programa envía caracteres al Arduino dependiendo del objeto detectado.

| Objeto detectado | Señal enviada |
|------------------|--------------|
| Círculo rojo | C |
| Rectángulo verde | R |
| Cuadrado azul | S |
| Ninguno | N |

Cuando se detecta un objeto válido también se activa el LED blanco.

---

## Conexión de LEDs

Los LEDs deben conectarse a los siguientes pines del Arduino:

| LED | Pin |
|----|----|
| Blanco | 7 |
| Rojo | 8 |
| Verde | 9 |
| Azul | 10 |

---

## Requisitos

Instalar las siguientes librerías de Python:
pip install opencv-python
pip install numpy
pip install pyserial


Ejecutar el archivo Python con:


python camara.py


Se abrirá una ventana con la cámara y el sistema comenzará a detectar objetos.

Para cerrar el programa presionar la tecla **ESC**.

---

## Ejemplo de detección

En pantalla se mostrará el nombre de la forma y el color detectado.

Ejemplo:


Circulo ROJO
Rectangulo VERDE
Cuadrado AZUL


En la terminal también aparecerá un mensaje indicando el objeto detectado:


Detectado: Circulo ROJO


---

## Resultado esperado

El sistema detecta correctamente:

- círculo rojo  
- rectángulo verde  
- cuadrado azul  

Si no hay ningún objeto frente a la cámara, el sistema no detecta nada y todos los LEDs permanecen apagados.
