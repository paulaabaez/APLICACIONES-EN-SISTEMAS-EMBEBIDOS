# Codigo phyton 

Para llegar a este codigo se investgo la parte de MediaPipe y sus puntos para detectar la persona, en base a ello se genera el siguiente codigo, donde se hace un archivo en blog de notas con la extension .py para poder llamarlo o ejecutarlo en la terminal.
En pocas palabras lo que hace en pasos resumidos es:

# Resumen general del código (qué hace de principio a fin)
## Importación de librerías: 
Se importan `cv2` (OpenCV) para manejo de video, `mediapipe` para detección de pose, `serial` para comunicación con Arduino, `time` para pausas y `collections.Counter` para suavizar resultados.

## Configuración inicial de MediaPipe: 
Se inicializa el módulo de pose de MediaPipe y se crea un objeto Pose con parámetros específicos (modo de imagen, complejidad, suavizado, umbrales de confianza).

## Conexión con Arduino: 
Se intenta establecer comunicación serial con el Arduino en un puerto específico (COM4). Si falla, el programa continúa pero sin control de LEDs.

## Función detectar_postura(landmarks): 
Recibe los puntos clave (landmarks) de la persona y determina si está de pie o sentada comparando la altura (coordenada Y) de caderas y rodillas. También verifica visibilidad.

## Función dibujar_info(frame, postura): 
Dibuja en el frame un rectángulo con el estado de la postura y, si hay Arduino, el color del LED correspondiente.

## Función principal `main()`:
Abre la cámara web.

Muestra instrucciones.

Inicia un bucle continuo para leer frames de la cámara.
### Por cada frame:

Lo voltea horizontalmente (efecto espejo).

Lo convierte a RGB (MediaPipe trabaja con RGB).

Procesa con MediaPipe para obtener landmarks.

Si detecta una persona, dibuja los puntos y conexiones.

Llama a detectar_postura() para obtener la postura del frame actual.

Mantiene un historial de las últimas 5 detecciones y usa Counter para elegir la más frecuente (suavizado).

Si hay cambio de postura y Arduino está conectado, envía por serial 'R' (rojo) o 'G' (verde).

Dibuja la información en pantalla con dibujar_info().

Si no detecta persona, muestra mensaje "Sin persona".

Espera la tecla 'q' para salir.

Al salir, libera la cámara, cierra ventanas y cierra la conexión serial.

Ejecución: Se llama a main() solo si el script se ejecuta directamente.

```python
"""
TAREA COMPLETA - Pose Detection con Arduino
Autor: [PaulaBaez]
"""

import cv2
import mediapipe as mp
import serial
import time
from collections import Counter

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================
print("="*50)
print("INICIANDO PROGRAMA")
print("="*50)

# Inicializar MediaPipe
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

# Crear detector
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

print("✅ MediaPipe listo")

# ============================================
# CONEXIÓN ARDUINO
# ============================================
PUERTO_ARDUINO = 'COM4'  # IMPORTANTE: CAMBIA ESTO

try:
    arduino = serial.Serial(PUERTO_ARDUINO, 9600, timeout=1)
    time.sleep(2)
    print(f"✅ Arduino conectado en {PUERTO_ARDUINO}")
    arduino_conectado = True
except:
    print(f"⚠️ No se pudo conectar a Arduino en {PUERTO_ARDUINO}")
    print("   El programa funcionará sin LEDs")
    arduino_conectado = False
    arduino = None

# ============================================
# FUNCIÓN PARA DETECTAR POSTURA
# ============================================
def detectar_postura(landmarks):
    """
    Detecta si la persona está de pie o sentada
    """
    
    # Obtener puntos clave
    cadera_izq = landmarks[23].y
    cadera_der = landmarks[24].y
    rodilla_izq = landmarks[25].y
    rodilla_der = landmarks[26].y
    
    # Promedios
    cadera_y = (cadera_izq + cadera_der) / 2
    rodilla_y = (rodilla_izq + rodilla_der) / 2
    
    # Verificar visibilidad
    if (landmarks[23].visibility < 0.5 or 
        landmarks[24].visibility < 0.5):
        return "NO SEGURO"
    
    # LÓGICA PRINCIPAL
    # Si cadera está arriba de rodillas -> DE PIE
    # Si cadera está abajo -> SENTADO
    
    print(f"📊 Cadera Y: {cadera_y:.3f}, Rodilla Y: {rodilla_y:.3f}")
    
    if cadera_y < rodilla_y - 0.1:
        return "DE PIE"
    elif cadera_y > rodilla_y + 0.1:
        return "SENTADO"
    else:
        if cadera_y < rodilla_y:
            return "DE PIE"
        else:
            return "SENTADO"

# ============================================
# FUNCIÓN PARA DIBUJAR ETIQUETA
# ============================================
def dibujar_info(frame, postura):
    """
    Dibuja la información en pantalla
    """
    
    # Configurar colores
    if postura == "DE PIE":
        color = (0, 0, 255)  # Rojo
        texto = "⬆️ DE PIE"
    elif postura == "SENTADO":
        color = (0, 255, 0)  # Verde
        texto = "⬇️ SENTADO"
    else:
        color = (128, 128, 128)  # Gris
        texto = "❓ DETECTANDO"
    
    # Rectángulo de fondo
    cv2.rectangle(frame, (10, 10), (300, 80), color, -1)
    
    # Texto principal
    cv2.putText(frame, texto, (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Indicador Arduino
    if arduino_conectado:
        led = "LED: 🔴" if postura == "DE PIE" else "LED: 🟢" if postura == "SENTADO" else "LED: ⚪"
        cv2.putText(frame, led, (20, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

# ============================================
# PROGRAMA PRINCIPAL
# ============================================
def main():
    print("\n🎥 Iniciando cámara...")
    
    # Abrir cámara
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ ERROR: No se pudo abrir la cámara")
        return
    
    print("✅ Cámara lista")
    print("\n📌 INSTRUCCIONES:")
    print("   - Párate frente a la cámara → LED ROJO")
    print("   - Siéntate frente a la cámara → LED VERDE")
    print("   - Presiona 'q' para salir")
    print("-" * 40)
    
    # Variables
    historial = []
    postura_actual = "DESCONOCIDO"
    
    while True:
        # Leer cámara
        ret, frame = cap.read()
        if not ret:
            break
            
        # Efecto espejo
        frame = cv2.flip(frame, 1)
        
        # Convertir a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Procesar con MediaPipe
        resultados = pose.process(frame_rgb)
        
        # Si hay persona
        if resultados.pose_landmarks:
            # Dibujar puntos del cuerpo
            mp_draw.draw_landmarks(
                frame, 
                resultados.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )
            
            # Detectar postura
            postura = detectar_postura(resultados.pose_landmarks.landmark)
            
            # Suavizar con historial
            if postura != "NO SEGURO":
                historial.append(postura)
                if len(historial) > 5:
                    historial.pop(0)
            
            if historial:
                # Obtener postura más común
                contador = Counter(historial)
                postura_final = contador.most_common(1)[0][0]
            else:
                postura_final = "DESCONOCIDO"
            
            # Enviar a Arduino si cambió
            if arduino_conectado and postura_final != postura_actual:
                postura_actual = postura_final
                if postura_final == "DE PIE":
                    arduino.write(b'R')
                    print("🔴 Enviado: ROJO")
                elif postura_final == "SENTADO":
                    arduino.write(b'G')
                    print("🟢 Enviado: VERDE")
            
            # Dibujar información
            dibujar_info(frame, postura_final)
            
        else:
            cv2.putText(frame, "Sin persona", (50, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Mostrar
        cv2.imshow('TAREA - Pose Detection', frame)
        
        # Tecla para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Limpiar
    cap.release()
    cv2.destroyAllWindows()
    if arduino_conectado:
        arduino.close()
    print("\n✅ Programa terminado")

# ============================================
# EJECUTAR
# ============================================
if __name__ == "__main__":

    main()

