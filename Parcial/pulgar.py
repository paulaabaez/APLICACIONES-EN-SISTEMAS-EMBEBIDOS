"""
DETECTOR DE PULGAR - Versión explicada
Muestra puntos rojos solamente en el pulgar usando la cámara
"""

# Importar librerías necesarias
import cv2  # OpenCV para manejo de cámara y dibujo
import mediapipe as mp  # MediaPipe para detección de manos

# Configurar MediaPipe para detección de manos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,  # Modo video (no imágenes estáticas)
    max_num_hands=2,           # Detectar máximo 2 manos
    min_detection_confidence=0.5,  # Confianza mínima 50%
    min_tracking_confidence=0.5     # Confianza mínima para seguimiento
)

# Índices de los puntos del pulgar según MediaPipe
# 1: base, 2: falange 1, 3: falange 2, 4: punta
PULGAR = [1, 2, 3, 4]

# Abrir la cámara (0 = cámara por defecto)
cap = cv2.VideoCapture(0)

# Verificar que la cámara se abrió correctamente
if not cap.isOpened():
    print("ERROR: No se pudo abrir la cámara")
    exit()

# Mensajes de inicio
print("=== DETECTOR DE PULGAR ===")
print("Presiona 'q' para salir")
print("Mostrando puntos SOLO en el pulgar...")

# Bucle principal: procesar cada frame de la cámara
while True:
    # Leer un frame de la cámara
    ret, frame = cap.read()
    
    # Si no se pudo leer, salir
    if not ret:
        print("Error al leer la cámara")
        break
    
    # Voltear la imagen horizontalmente (efecto espejo)
    frame = cv2.flip(frame, 1)
    
    # Convertir de BGR (OpenCV) a RGB (MediaPipe)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detectar manos en el frame
    results = hands.process(frame_rgb)
    
    # Si se detectaron manos
    if results.multi_hand_landmarks:
        # Recorrer cada mano detectada
        for hand_landmarks in results.multi_hand_landmarks:
            # Obtener dimensiones del frame
            h, w, _ = frame.shape
            
            # Recorrer solo los puntos del pulgar
            for idx in PULGAR:
                # Obtener el punto específico
                landmark = hand_landmarks.landmark[idx]
                
                # Convertir coordenadas normalizadas a píxeles
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                
                # Dibujar círculo rojo relleno
                cv2.circle(frame, (x, y), 12, (0, 0, 255), -1)
                # Dibujar borde blanco para que resalte
                cv2.circle(frame, (x, y), 12, (255, 255, 255), 2)
    
    # Mostrar instrucciones en la imagen
    cv2.putText(frame, "Puntos rojos = Pulgar", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, "Presiona 'q' para salir", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Mostrar la imagen en una ventana
    cv2.imshow('Detector de Pulgar', frame)
    
    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
print("Programa terminado")