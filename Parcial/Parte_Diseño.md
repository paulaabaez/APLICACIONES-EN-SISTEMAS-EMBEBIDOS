2.Plantee una solución paso a paso de las situaciones descritas con lo aprendido en clase:
2.1¿Como plantearía el desarrollo de una base de datos con imágenes de los diferentes elementos de un laboratorio de telecomunicaciones?

Paso a Paso
 
Definición de Clases: Lo primero es listar y categorizar todos los elementos que se desean reconocer.

Herramientas: Multímetros, Osciloscopios, Analizadores de Espectro, Generadores de Señales, Fuentes de Alimentación, Estaciones de Soldadura, Pinzas, Cortafrío, etc.

Personas: Se pueden definir como una sola clase ("persona") o, si se requiere identificación, como clases individuales (ej. "Juan", "María").

Elementos Fijos: Puertas, Mesas, Sillas (útiles para contextualizar la escena).

Captura de Imágenes (Data Acquisition):

Fuentes Múltiples: Usar la cámara que se instalará en el laboratorio (punto de vista fijo) para capturar imágenes en diferentes condiciones de iluminación (mañana, tarde, noche) y con diferentes ángulos de las herramientas (sobre la mesa, en la mano, en el estante).

Aumento de Datos (Data Augmentation): Para enriquecer el dataset sin tomar más fotos, se aplican transformaciones a las imágenes existentes usando librerías como imgaug o TensorFlow/Keras. Ej: rotaciones leves, cambios de brillo, zoom, desplazamientos horizontales/verticales. Esto ayuda al modelo a generalizar mejor.

Anotación de Imágenes (Labeling):

Para un sistema clasificador, cada imagen necesita una etiqueta (ej. osciloscopio_001.jpg -> clase: "osciloscopio").

Herramientas de Anotación: Usar software como LabelImg o CVAT para dibujar recuadros (bounding boxes) alrededor de cada objeto y persona en la imagen, y asignarles la clase correspondiente. Este proceso genera un archivo (en formato XML o JSON) por imagen.

Organización y Almacenamiento:

Estructurar el dataset en carpetas. Por ejemplo:

text
dataset_laboratorio/
├── train/
│   ├── osciloscopio/ (imagenes y anotaciones)
│   ├── multimetro/
│   ├── persona/
│   └── ...
└── validation/ (misma estructura que train)
Almacenar este dataset en un lugar accesible para el entrenamiento (disco duro local, o en la nube como Google Drive o AWS S3).

2.2¿Como  crearía un sistema clasificador de elementos con la librería media pipe?

Paso a Paso:

Elección de la Tarea: Para identificar múltiples herramientas en una imagen, necesitamos detección de objetos (localizar y clasificar). MediaPipe Tasks ofrece una solución lista para esto.

Entrenamiento del Modelo (opcional pero recomendado):

Si el dataset es de herramientas específicas, se puede entrenar un modelo custom. MediaPipe ofrece herramientas para entrenar modelos de detección de objetos (basados en SSD, EfficientDet-Lite) usando el conjunto de datos anotado del paso anterior.

Formato: El dataset debe convertirse al formato TFRecord, que es el que usa TensorFlow (el backend de MediaPipe) para el entrenamiento.

Implementación con MediaPipe Tasks:

Una vez entrenado el modelo (o usando uno pre-entrenado de la galería de MediaPipe si es suficiente), se utiliza la librería mediapipe en Python.

Código Conceptual:

python
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.vision import ObjectDetector, RunningMode

# Configurar el detector
options = python.vision.ObjectDetectorOptions(
    base_options=python.BaseOptions(model_asset_path='modelo_herramientas.tflite'),
    running_mode=RunningMode.IMAGE, # o VIDEO para detección continua
    max_results=5,
    score_threshold=0.5)
detector = ObjectDetector.create_from_options(options)

# Procesar una imagen
image = mp.Image.create_from_file('imagen_laboratorio.jpg')
detection_result = detector.detect(image)

# Resultado: Lista de objetos detectados con bounding boxes y etiquetas (ej. "osciloscopio", "persona")
for detection in detection_result.detections:
    print(detection.categories[0].category_name)
Este sistema puede ejecutarse en el sistema embebido (si tiene capacidad, como una Raspberry Pi) o en un servidor central que reciba las imágenes.


2.3¿Como reconocería el sistema la velocidad de las personas en el laboratorio?

Primero necesito seguir a cada persona a lo largo del tiempo. El detector de MediaPipe me da la posición de la persona en cada fotograma, pero eso no es suficiente porque si hay dos personas, debo saber cuál es cuál en el siguiente fotograma. Para eso utilizo un tracker, que es un algoritmo que asigna un identificador único a cada persona y va actualizando su posición a medida que se mueve. MediaPipe tiene un tracker integrado, pero también se puede usar OpenCV que ofrece varias opciones.

Una vez que tengo la trayectoria de cada persona en píxeles, necesito convertir esas distancias a unidades del mundo real, es decir, a metros. La cámara no sabe cuánto mide un píxel en la realidad, así que tengo que calibrarla. Una forma sencilla es medir un objeto de referencia. Por ejemplo, si sé que una puerta del laboratorio mide 2 metros de alto y en la imagen ocupa 400 píxeles, entonces cada píxel equivale a 0.005 metros en esa zona de la imagen. No es una medida exacta porque la perspectiva varía, pero para tener una aproximación y detectar movimientos bruscos es suficiente.

Con esa relación, calculo el desplazamiento de la persona entre un fotograma y el siguiente. Si en el fotograma anterior estaba en una posición y en el actual está en otra, la diferencia en píxeles la convierto a metros usando el factor de escala. Luego divido esa distancia por el tiempo transcurrido entre fotogramas, que es el inverso de los cuadros por segundo de la cámara. El resultado es la velocidad instantánea en metros por segundo.

Finalmente defino un umbral. Si alguien se mueve a más de, digamos, 2 metros por segundo, considero que es un movimiento rápido y activo una alerta. Esa alerta puede mostrarse en pantalla, guardarse en un archivo de registro o incluso enviarse como notificación si el sistema está conectado a una red.

2.4¿Como haría un despliegue en una plataforma web o móvil? 
 
Para que la información sea accesible desde cualquier lugar, el sistema debe desplegarse en una plataforma que pueda consultarse desde el celular o el navegador.

La idea es tener una computadora en el laboratorio conectada a la cámara. Esta computadora se encarga de todo el procesamiento pesado: correr el modelo de MediaPipe, hacer el seguimiento de personas, calcular velocidades y generar alertas. Además, en esa misma máquina levanto un servidor con Flask o FastAPI que exponga los datos a través de una API REST.

La API tiene varios endpoints. Por ejemplo, uno que devuelva la lista de herramientas detectadas en el último frame, otro que devuelva las personas con su posición y velocidad actual, y otro que dé las últimas alertas generadas. Cada vez que alguien consulte estos endpoints, el servidor responde con datos en formato JSON.

Por otro lado, desarrollo una interfaz web sencilla con HTML, CSS y JavaScript. En esta interfaz puedo mostrar el video en vivo del laboratorio usando una etiqueta de video, y sobre él dibujar los recuadros y etiquetas usando un canvas. Para actualizar la información, la página consulta la API cada cierto tiempo, por ejemplo cada medio segundo, y vuelve a pintar los recuadros con los nuevos datos. También puedo agregar un panel lateral que muestre las herramientas detectadas y las alertas de velocidad.

Si quiero tener una aplicación móvil, desarrollo una app con Flutter o React Native que consuma la misma API. La lógica es la misma, solo que adaptada a una pantalla táctil. De esta forma, cualquier persona con acceso a la red del laboratorio puede abrir la app o la página web y ver en tiempo real lo que está pasando, qué herramientas hay sobre las mesas y si alguien se está moviendo de manera peligrosa.

Este enfoque tiene la ventaja de que separa claramente la parte pesada del procesamiento de la parte liviana de visualización. Si después quiero agregar más funcionalidades, como guardar un histórico o generar reportes, puedo hacerlo sin afectar lo que ya funciona.
