# Clasificación de Objetos en Tiempo Real con YOLOv8

## Descripción del proyecto
Este proyecto consiste en el desarrollo de un sistema de visión artificial capaz de detectar y clasificar objetos en tiempo real utilizando el modelo YOLOv8. La detección se realiza mediante la cámara del computador y permite identificar objetos como personas, vehículos y bicicletas.

Posteriormente, estos objetos son reinterpretados dentro de una lógica personalizada para clasificarlos como juguetes, asignando además un color específico a cada categoría para mejorar la visualización.

---

## Objetivo general
Desarrollar un sistema de detección y clasificación de objetos en tiempo real utilizando inteligencia artificial.

## Objetivos específicos
- Implementar un modelo de detección de objetos (YOLOv8)
- Capturar video en tiempo real desde la cámara
- Clasificar objetos en categorías personalizadas
- Visualizar resultados mediante recuadros y etiquetas
- Diferenciar clases mediante colores

---

## Tecnologías utilizadas
- Python 3.11
- OpenCV
- YOLOv8 
- Visual Studio Code

---

## Componentes utilizados

### Software
- Python
- Librerías:
  - ultralytics
  - opencv-python
  - numpy

### Hardware
- Computador
- Cámara web (integrada o externa)

---

## Instalación del entorno

### 1. Instalación de Python
Descargar desde:
https://www.python.org/

Verificar instalación:

python --version

---

## Instalación de Visual Studio Code

- Descargar desde:
- https://code.visualstudio.com/

---

## Instalación de librerías

### Ejecutar en la terminal:

- pip install numpy==1.26.4
- pip install opencv-python==4.8.0.76
- pip install ultralytics

---

# Estructura del proyecto

clasificacion_yolo/
│
├── main.py
├── README.md
└── imagenes/
    ├── resultado1.png
    └── resultado2.png

# Código principal (main.py)
import cv2
from ultralytics import YOLO

def clasificar_y_color(nombre):
    if nombre == "person":
        return "Persona", (0,255,0)
    
    elif nombre == "car":
        return "Carro de juguete", (255,0,0)
    
    elif nombre == "motorcycle":
        return "Moto de juguete", (0,0,255)
    
    elif nombre == "bicycle":
        return "Bicicleta de juguete", (0,255,255)
    
    elif nombre == "bus":
        return "Bus de juguete", (255,0,255)

    elif nombre in ["truck", "train"]:
        return "Vehiculo (posible juguete)", (255,255,0)

    else:
        return None, None

modelo = YOLO("yolov8s.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resultados = modelo(frame, stream=True, conf=0.3)

    for r in resultados:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            clase = int(box.cls[0])
            nombre = modelo.names[clase]

            etiqueta, color = clasificar_y_color(nombre)

            if etiqueta:
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{etiqueta} {conf:.2f}",
                            (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, color, 2)

    cv2.imshow("Clasificacion YOLO", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

![evidencia codigo 1](https://github.com/user-attachments/assets/98a5c2af-e1df-4e56-a096-224af9e313f2)
![evidencia codigo 2](https://github.com/user-attachments/assets/11baa424-81b5-438b-818f-5ac79954ebe8)

---

## Funcionamiento del sistema

1. Se activa la cámara del computador  
2. Se capturan imágenes en tiempo real  
3. YOLO analiza cada frame  
4. Detecta objetos en la escena  
5. Identifica la clase original  
6. Se transforma a una categoría personalizada  
7. Se dibuja un recuadro  
8. Se asigna un color  
9. Se muestra en pantalla  

---

## Clasificación y colores

| Objeto detectado | Clasificación | Color |
|-----------------|--------------|------|
| person          | Persona | Verde |
| car             | Carro de juguete | Azul |
| motorcycle      | Moto de juguete | Rojo |
| bicycle         | Bicicleta de juguete | Amarillo |
| bus             | Bus de juguete | Morado |

---

## Imágenes del sistema

Guardar imágenes en la carpeta `imagenes`:

imagenes/
 ├── resultado1.png
 └── resultado2.png
---

## Problemas encontrados

- Incompatibilidad entre numpy y opencv  
- Baja detección en objetos pequeños  
- Confusión entre clases similares  

---

## Soluciones implementadas

- Uso de numpy 1.26.4  
- Uso de opencv 4.8.0.76  
- Uso de yolov8s  
- Ajuste de confianza (0.3)  
- Clasificación personalizada  

---

## Conclusiones

El sistema permite detectar objetos en tiempo real de forma eficiente. Para mejorar la precisión en objetos específicos como juguetes, es recomendable entrenar un modelo personalizado.

---

## Mejoras futuras

- Entrenamiento con dataset propio  
- Mejora en detección de objetos pequeños  
- Interfaz gráfica  
- Guardado de resultados

---
