# Habitación Inteligente con ESP32

Proyecto de domótica con ESP32 que integra:

## Funciones
-  Control de luz (LED)
-  Control de persiana (Servo)
-  Activación por sonido (micrófono A0)
-  Reloj en tiempo real (RTC DS3231)

## Componentes
- ESP32
- Servo SG90
- LED + resistencia
- Sensor de sonido (A0)
- Módulo RTC DS3231

## Conexiones

### LED
GPIO 23 → resistencia → LED → GND

### Servo
Rojo → 5V  
Marrón → GND  
Naranja → GPIO 18  

### Micrófono
VCC → 3.3V  
GND → GND  
A0 → GPIO 34  

### RTC DS3231
VCC → 3.3V  
GND → GND  
SDA → GPIO 21  
SCL → GPIO 22  

## Funcionamiento
- Detecta sonido → cambia estado (ON/OFF)
- Controla luz y persiana
- Muestra hora en monitor serial

## Evidencia maqueta

<img width="1600" height="1200" alt="2" src="https://github.com/user-attachments/assets/dfe5eeec-f9c1-4e5b-8f65-f1c3eb0d12b7" />

## Evidencia circuito

<img width="1600" height="1200" alt="1" src="https://github.com/user-attachments/assets/672a95d7-c870-4a32-8f83-37a4ae52c996" />

## Nota
Ajustar el umbral de sonido según el entorno.

## Autor
Paula Baez
