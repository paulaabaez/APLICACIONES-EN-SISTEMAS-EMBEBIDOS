"""
DETECTOR DE PULGAR - Versión simple
Muestra puntos rojos solamente en el pulgar
"""

import cv2
import mediapipe as mp

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Índices del pulgar (según MediaPipe)
PULGAR = [1, 2, 3, 4]  # 1=base, 2=segunda falange, 3=tercera, 4=punta

# Abrir cámara
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: No se pudo abrir la cámara")
    print("Prueba cambiando el número: VideoCapture(1) o VideoCapture(2)")
    exit()

print("=== DETECTOR DE PULGAR ===")
print("Presiona 'q' para salir")
print("Mostrando puntos SOLO en el pulgar...")

while True:
    # Leer frame de la cámara
    ret, frame = cap.read()
    if not ret:
        print("Error al leer la cámara")
        break
    
    # Voltear imagen (efecto espejo)
    frame = cv2.flip(frame, 1)
    
    # Convertir a RGB (MediaPipe usa RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detectar manos
    results = hands.process(frame_rgb)
    
    # Si hay manos detectadas
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            h, w, _ = frame.shape
            
            # Dibujar SOLO los puntos del pulgar
            for idx in PULGAR:
                landmark = hand_landmarks.landmark[idx]
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                
                # Dibujar punto rojo
                cv2.circle(frame, (x, y), 12, (0, 0, 255), -1)
                
                # Opcional: pequeño borde blanco para que resalte
                cv2.circle(frame, (x, y), 12, (255, 255, 255), 2)
    
    # Mostrar instrucciones en pantalla
    cv2.putText(frame, "Puntos rojos = Pulgar", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, "Presiona 'q' para salir", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Mostrar resultado
    cv2.imshow('Detector de Pulgar', frame)
    
    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
print("Programa terminado")