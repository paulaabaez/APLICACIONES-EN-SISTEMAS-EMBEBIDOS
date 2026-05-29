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

#Codigo

/*
Proyecto Casa Inteligente ESP32
OLED + RTC + Servo + RGB + LED Habitación
*/

#include <ESP32Servo.h>
#include <Wire.h>
#include <RTClib.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

RTC_DS3231 rtc;

Adafruit_SSD1306 display(
128,
64,
&Wire,
-1
);

Servo persiana;

String modo="MANANA";

String ultimoComando="NINGUNO";

bool habitacion=false;

bool persianaAbierta=false;

#define LED_HAB 23

#define RGB_R 14
#define RGB_G 12
#define RGB_B 13

void actualizarRGB(){

digitalWrite(
RGB_R,
LOW
);

digitalWrite(
RGB_G,
LOW
);

digitalWrite(
RGB_B,
LOW
);

if(
modo=="MANANA"
){

digitalWrite(
RGB_B,
HIGH
);

}

else if(
modo=="SPA"
){

digitalWrite(
RGB_R,
HIGH
);

}

else if(
modo=="NOCHE"
){

digitalWrite(
RGB_G,
HIGH
);

}

}

void procesarComando(
String comando
){

comando.trim();

comando.toLowerCase();

ultimoComando=
comando;

if(
comando=="spa" ||
comando=="modo spa"
){

modo="SPA";

actualizarRGB();

}

else if(
comando=="manana" ||
comando=="mañana" ||
comando=="modo manana"
){

modo="MANANA";

actualizarRGB();

}

else if(
comando=="noche" ||
comando=="modo noche"
){

modo="NOCHE";

actualizarRGB();

}

else if(
comando=="encender"
){

habitacion=true;

digitalWrite(
LED_HAB,
HIGH
);

}

else if(
comando=="apagar"
){

habitacion=false;

digitalWrite(
LED_HAB,
LOW
);

}

else if(
comando=="abrir"
){

persiana.write(
90
);

persianaAbierta=true;

}

else if(
comando=="cerrar"
){

persiana.write(
0
);

persianaAbierta=false;

}

}

void leerSerial(){

if(
Serial.available()
){

String comando=
Serial.readStringUntil(
'\n'
);

procesarComando(
comando
);

}

}

void setup(){

Serial.begin(
115200
);

pinMode(
LED_HAB,
OUTPUT
);

pinMode(
RGB_R,
OUTPUT
);

pinMode(
RGB_G,
OUTPUT
);

pinMode(
RGB_B,
OUTPUT
);

Wire.begin(
21,
22
);

display.begin(
SSD1306_SWITCHCAPVCC,
0x3C
);

rtc.begin();

/*
Descomenta una sola vez
para ajustar hora
*/

// rtc.adjust(
// DateTime(
// F(__DATE__),
// F(__TIME__)
// )
// );

persiana.attach(
18,
500,
2400
);

persiana.write(
0
);

actualizarRGB();

Serial.println(
"Sistema iniciado"
);

}

void loop(){

leerSerial();

DateTime now=
rtc.now();

display.clearDisplay();

display.setTextSize(
1
);

display.setTextColor(
WHITE
);

display.setCursor(
0,
0
);

display.print(
"Hora: "
);

if(
now.hour()<10
)
display.print("0");

display.print(
now.hour()
);

display.print(":");

if(
now.minute()<10
)
display.print("0");

display.print(
now.minute()
);

display.print(":");

if(
now.second()<10
)
display.print("0");

display.println(
now.second()
);

display.setCursor(
0,
15
);

display.print(
"Modo: "
);

display.println(
modo
);

display.setCursor(
0,
28
);

display.print(
"Hab: "
);

display.println(
habitacion ?
"ON":"OFF"
);

display.setCursor(
0,
41
);

display.print(
"Persiana:"
);

display.println(
persianaAbierta ?
"ABIERTA":
"CERRADA"
);

display.setCursor(
0,
54
);

display.print(
"Cmd:"
);

display.println(
ultimoComando
);

display.display();

delay(
100
);

}

Comandos por voz:

spa
mañana
noche
abrir
cerrar
encender
apagar

Evidencia nube
<img width="1365" height="623" alt="nube }" src="https://github.com/user-attachments/assets/bde809b2-2797-4141-855e-f95432ac6564" />


Autor: Paula
*/
