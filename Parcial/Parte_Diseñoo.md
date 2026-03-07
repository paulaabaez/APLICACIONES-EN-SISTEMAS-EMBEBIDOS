Sistema de Monitoreo Inteligente para Laboratorio de Telecomunicaciones
2. Planteamiento paso a paso de las situaciones descritas
A continuación, se presenta una solución detallada basada en los conceptos aprendidos en clase para abordar los diferentes desafíos planteados.

2.1 ¿Cómo plantearía el desarrollo de una base de datos con imágenes de los diferentes elementos de un laboratorio de telecomunicaciones?
Paso a Paso 

Definición de Clases:
Lo primero es listar y categorizar todos los elementos que se desean reconocer en el laboratorio.

Herramientas: Multímetros, Osciloscopios, Analizadores de Espectro, Generadores de Señales, Fuentes de Alimentación, Estaciones de Soldadura, Pinzas, Cortafrío, etc.

Personas: Se pueden definir como una sola clase ("persona") o, si se requiere identificación específica, como clases individuales (ej. "Juan", "María").

Elementos Fijos: Puertas, Mesas, Sillas (útiles para contextualizar la escena).

Captura de Imágenes:

Fuentes Múltiples: Usar la cámara que se instalará en el laboratorio (punto de vista fijo) para capturar imágenes en diferentes condiciones de iluminación (mañana, tarde, noche) y con diferentes ángulos de las herramientas (sobre la mesa, en la mano de una persona, en el estante).

Aumento de Datos (Data Augmentation): Para enriquecer el dataset sin necesidad de tomar más fotos físicamente, se aplican transformaciones a las imágenes existentes usando librerías como imgaug o las herramientas de TensorFlow/Keras. Por ejemplo: rotaciones leves, cambios de brillo, zoom, desplazamientos horizontales/verticales. Esto ayuda al modelo a generalizar mejor y ser más robusto.

Anotación de Imágenes:

Para un sistema de clasificación básico, cada imagen necesitaría una etiqueta simple (ej. osciloscopio_001.jpg -> clase: "osciloscopio").

Para un sistema de detección (más útil en este caso), es necesario un etiquetado más detallado. Usando herramientas de anotación como LabelImg o CVAT, se dibujan recuadros (bounding boxes) alrededor de cada objeto y persona en la imagen, asignándoles la clase correspondiente. Este proceso genera un archivo (en formato XML o JSON) por imagen que contiene la ubicación y etiqueta de cada elemento.

Organización y Almacenamiento:
Estructurar el dataset en carpetas de forma ordenada para facilitar su uso durante el entrenamiento. Por ejemplo:

text
dataset_laboratorio/
├── train/
│   ├── osciloscopio/ (aqui van las imagenes y sus anotaciones)
│   ├── multimetro/
│   ├── persona/
│   └── ...
└── validation/ (con la misma estructura que 'train')
Finalmente, almacenar este dataset en un lugar accesible para el proceso de entrenamiento, como un disco duro local, o en la nube (Google Drive, Amazon S3, etc.).

2.2 ¿Cómo crearía un sistema clasificador de elementos con la librería MediaPipe?
Paso a Paso 

Elección de la Tarea: Para identificar múltiples herramientas y personas en una imagen, necesitamos un sistema de detección de objetos (que no solo clasifique, sino que también localice cada elemento). MediaPipe Tasks ofrece soluciones listas para esto.

Entrenamiento del Modelo:

Si el dataset contiene herramientas específicas del laboratorio, lo óptimo es entrenar un modelo personalizado (custom model). MediaPipe proporciona herramientas para entrenar modelos de detección de objetos (basados en arquitecturas como SSD o EfficientDet-Lite) utilizando el conjunto de datos anotado en el paso anterior.

Formato: El dataset (imágenes y anotaciones) debe convertirse al formato TFRecord, que es el estándar que utiliza TensorFlow (el backend de MediaPipe) para el entrenamiento eficiente.

Implementación con MediaPipe Tasks:
Una vez entrenado el modelo (o si se opta por usar uno pre-entrenado de la galería de MediaPipe), se utiliza la librería mediapipe en Python para la inferencia.

Código Conceptual:

python
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.vision import ObjectDetector, RunningMode

# Configurar el detector con nuestro modelo entrenado
options = python.vision.ObjectDetectorOptions(
    base_options=python.BaseOptions(model_asset_path='modelo_herramientas.tflite'),
    running_mode=RunningMode.IMAGE, # Usar 'VIDEO' para detección en tiempo real
    max_results=5,
    score_threshold=0.5) # Confianza mínima del 50%

# Crear el detector
detector = ObjectDetector.create_from_options(options)

# Cargar y procesar una imagen
image = mp.Image.create_from_file('imagen_laboratorio.jpg')
detection_result = detector.detect(image)

# Mostrar resultados: lista de objetos detectados
for detection in detection_result.detections:
    print(f"Objeto detectado: {detection.categories[0].category_name} "
          f"con una confianza de: {detection.categories[0].score:.2f}")
Este sistema puede ejecutarse en el sistema embebido del laboratorio (si tiene suficiente capacidad, como una Raspberry Pi 4/5) o en un servidor central que reciba y procese las imágenes de la cámara.

2.3 ¿Cómo reconocería el sistema la velocidad de las personas en el laboratorio?
Paso a Paso 

Seguimiento de Personas (Tracking):
El detector de MediaPipe nos da la posición de una persona en un fotograma, pero no sabe si esa persona es la misma que aparecía en el fotograma anterior. Para lograr esto, necesitamos un algoritmo de seguimiento (tracker). Este asigna un identificador único (ID) a cada persona y va actualizando su posición a medida que se mueve. MediaPipe tiene trackers integrados, pero también se pueden usar implementaciones de OpenCV (como los trackers CSRT, KCF, etc.) para mayor control.

Calibración Píxel-Metro:
Para convertir el movimiento en píxeles a una velocidad en el mundo real (m/s), es necesario calibrar la cámara. Una forma sencilla es usar un objeto de referencia de dimensiones conocidas.

Por ejemplo, si sabemos que una puerta del laboratorio mide 2 metros de alto y en la imagen ocupa 400 píxeles, entonces, como aproximación inicial, cada píxel equivale a 2 m / 400 px = 0.005 m/px en esa zona. Este factor no es perfecto debido a la perspectiva, pero es suficiente para detectar movimientos bruscos.

Cálculo de Velocidad:
Con la trayectoria y la calibración, calculamos la velocidad instantánea entre fotogramas.

Desplazamiento real (metros): (Posición_actual_en_px - Posición_anterior_en_px) * Factor_de_escala (m/px)

Tiempo transcurrido (segundos): 1 / Fotogramas_por_segundo (FPS) de la cámara

Velocidad (m/s): Desplazamiento_real / Tiempo_transcurrido

Definición de Umbral y Alerta:
Finalmente, se define un umbral de velocidad considerado seguro o normal para el laboratorio (ej. 2 m/s, que es un paso rápido pero no una carrera). Si la velocidad calculada para una persona supera este umbral, el sistema activa una alerta. Esta alerta puede mostrarse en pantalla, guardarse en un archivo de registro (log) o incluso enviarse como notificación si el sistema está conectado a una red.

2.4 ¿Cómo haría un despliegue en una plataforma web o móvil?
Paso a Paso 

Para que la información del laboratorio sea accesible desde cualquier lugar (aula, casa, etc.), el sistema debe desplegarse en una plataforma accesible vía web o móvil.

Servidor de Procesamiento Local:
Una computadora en el laboratorio (conectada a la cámara) se encarga de todo el procesamiento pesado: ejecutar el modelo de MediaPipe para la detección, realizar el seguimiento de personas, calcular velocidades y generar alertas. En esta misma máquina, se levanta un servidor web ligero (por ejemplo, con Flask o FastAPI) que expone los datos a través de una API REST.

API REST (Backend):
La API tendrá varios endpoints que el frontend (web o móvil) podrá consultar:

/api/herramientas: Devuelve la lista de herramientas detectadas en el último fotograma con sus ubicaciones.

/api/personas: Devuelve la lista de personas detectadas con su ID, posición y velocidad actual.

/api/alertas: Devuelve las últimas alertas generadas (por velocidad, o por objetos en zonas no permitidas).

/api/video/stream: Para servir el video en vivo.
Cada vez que se consulta un endpoint, el servidor responde con los datos en formato JSON.

Interfaz Web (Frontend):
Se desarrolla una interfaz web sencilla con HTML, CSS y JavaScript.

Visualización en vivo: Se usa la etiqueta <video> para mostrar el stream de la cámara.

Superposición de datos: Sobre el video, se usa un elemento <canvas> para dibujar en tiempo real los recuadros (bounding boxes), etiquetas (ej. "Osciloscopio") y la velocidad de las personas.

Actualización: La página web consulta la API cada cierto intervalo (por ejemplo, cada 0.5 segundos) mediante fetch() para obtener los datos más recientes y redibujar la información en el canvas.

Panel lateral: Se puede agregar un panel que muestre un listado de herramientas detectadas y las últimas alertas.

Aplicación Móvil:
Si se desea una experiencia nativa, se puede desarrollar una aplicación móvil con frameworks como Flutter o React Native. La lógica es la misma que la web: la aplicación consume los mismos endpoints de la API REST para obtener los datos del laboratorio y mostrarlos de forma adaptada a una pantalla táctil.

De esta forma, cualquier persona con acceso a la red del laboratorio puede abrir la aplicación o la página web y ver, en tiempo real, qué está sucediendo, qué herramientas hay sobre las mesas y si alguien se está moviendo de manera peligrosa. La gran ventaja de este enfoque es la clara separación entre el procesamiento pesado (servidor local) y la visualización liviana (cliente web/móvil), lo que facilita el mantenimiento y la escalabilidad del sistema.
