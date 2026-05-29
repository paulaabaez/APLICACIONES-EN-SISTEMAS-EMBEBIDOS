# Casa Inteligente ESP32 con Voz

Proyecto de automatización usando ESP32, reconocimiento básico por voz mediante micrófono INMP441, RTC, OLED, servo y control de iluminación.

## Funciones

- Habitación inteligente
- Baño inteligente
- Modos de iluminación
- Persiana automática
- Reloj en OLED
- Comandos por voz
- Estado mostrado en pantalla

## Componentes

- ESP32
- INMP441
- OLED SSD1306
- RTC DS3231
- Servo SG90
- LED RGB
- LED habitación
- Jumpers
- Fuente 5V

## Arquitectura

Micrófono → ESP32 → Procesamiento → Acción → OLED

## Comandos soportados

spa

mañana

noche

abrir

cerrar

encender

apagar

## Información mostrada en OLED

Hora: 14:25:10

Modo: SPA

Hab: ON

Persiana: ABIERTA

Voz: spa

# Conexiones completas

## INMP441

VDD -> 3.3V

GND -> GND

WS -> GPIO25

SCK -> GPIO26

SD -> GPIO33

L/R -> GND

## OLED SSD1306

SDA -> GPIO21

SCL -> GPIO22

VCC -> 3.3V

GND -> GND

## RTC DS3231

SDA -> GPIO21

SCL -> GPIO22

VCC -> 5V

GND -> GND

## Servo Persiana

Signal -> GPIO18

VCC -> 5V

GND -> GND

## LED Habitación

GPIO23

## RGB Baño

Rojo -> GPIO14

Verde -> GPIO12

Azul -> GPIO13

Casa-Inteligente-ESP32/
│
├── README.md
├── conexiones.md
├── librerias.txt
├── codigo/
│   └── casa_inteligente.ino
│
├── docs/
│   └── arquitectura.png
│
└── imagenes/

ESP32Servo
RTClib
Adafruit SSD1306
Adafruit GFX
Wire
driver/i2s
Bloque para poner al inicio de casa_inteligente.ino
/*

Proyecto: Casa Inteligente ESP32

Funciones:

- Comandos por voz simples
- Baño inteligente
- Habitación inteligente
- OLED con reloj
- Servo persiana
- RTC
- RGB
- Micrófono INMP441

Comandos por voz:

spa
mañana
noche
abrir
cerrar
encender
apagar

Autor: Paula
*/
