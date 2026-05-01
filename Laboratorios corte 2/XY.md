# Osciloscopio XY con ESP32

## Descripción
Este proyecto consiste en la implementación de un sistema capaz de dibujar figuras en un osciloscopio utilizando el modo XY mediante un microcontrolador ESP32.

El sistema genera señales analógicas en los ejes X y Y a partir de coordenadas previamente definidas, permitiendo visualizar trayectorias como figuras geométricas o formas complejas.

---

## Introducción
En este laboratorio se desarrolló un sistema de generación de señales analógicas utilizando el ESP32, sus convertidores digital-analógico (DAC) y un circuito de acondicionamiento con amplificadores operacionales.

Esto permite representar gráficamente trayectorias en un osciloscopio en modo XY.

---

## Objetivos

- Generar señales analógicas en los ejes X y Y  
- Implementar control mediante potenciómetros  
- Visualizar figuras en un osciloscopio  
- Comprender el uso de DAC, multiplexores y acondicionamiento de señal  

---

## Tecnologías utilizadas

- ESP32  
- Arduino IDE  
- SimulIDE (simulación)  
- Osciloscopio  
- DAC interno (GPIO 25 y 26)  

---

## Materiales

- ESP32  
- 2x MCP4725 (DAC)  
- CD74HC4067 (Multiplexor)  
- LM324N (Amplificador operacional)  
- 3 Potenciómetros  
- Protoboard  
- Cables  

---

## Conexión del sistema

### ESP32 → DAC

| ESP32 | DAC |
|------|-----|
| GPIO21 | SDA |
| GPIO22 | SCL |
| 3V3 | VCC |
| GND | GND |

---

### ESP32 → Multiplexor

| ESP32 | MUX |
|------|-----|
| GPIO18 | S0 |
| GPIO19 | S1 |
| GPIO23 | S2 |
| GPIO5  | S3 |
| GPIO34 | SIG |

---

### Potenciómetros

- POT1 → C0 (Escala X)  
- POT2 → C1 (Escala Y)  
- POT3 → C2 (Velocidad)  

---

## Funcionamiento

El sistema recorre una lista de coordenadas (X,Y) y las convierte en señales analógicas mediante el DAC del ESP32.

Estas señales controlan el movimiento del haz en el osciloscopio, permitiendo dibujar figuras en pantalla.

Los potenciómetros permiten ajustar:

- Escala en el eje X  
- Escala en el eje Y  
- Velocidad de trazado  

---

## Evidencia

### Simulación en SimulIDE

<img width="1230" height="1279" alt="image" src="https://github.com/user-attachments/assets/82815204-b2c2-4ddb-b92c-a37429e2cec4" />

### Resultados en osciloscopio

<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/45a409f3-bdda-40c9-81bd-f7378aa95792" />

<img width="3024" height="4032" alt="image" src="https://github.com/user-attachments/assets/d4869d40-2fa3-4415-930e-17b0e36f31f9" />

---

## Simulación

Se utilizó Arduino UNO en SimulIDE para simular el comportamiento del sistema, debido a la falta de soporte para ESP32 y DAC en dicho entorno.

En la simulación se empleó PWM (`analogWrite`) para aproximar las señales analógicas.

---

## Códigos

### Código de simulación (Arduino UNO)

```cpp
const int X = 9;
const int Y = 10;

void setup() {
  pinMode(X, OUTPUT);
  pinMode(Y, OUTPUT);
}

void loop() {
  for(int i=0;i<255;i++){
    analogWrite(X,i);
    analogWrite(Y,i);
    delay(5);
  }
}
```

---

### Código ESP32 (Salida DAC)

```cpp
const int DAC_X = 25; 
const int DAC_Y = 26;

struct Punto {
  uint8_t x;
  uint8_t y;
};

Punto trayectoria[] = {
  {47, 10},
  {49, 10}
  // ... (resto de puntos)
};

const int numPuntos = sizeof(trayectoria) / sizeof(trayectoria[0]);

void setup() {}

void loop() {
  for (int i = 0; i < numPuntos; i++) {
    dacWrite(DAC_X, trayectoria[i].x);
    dacWrite(DAC_Y, trayectoria[i].y);
    delayMicroseconds(20);
  }
}
```

---

## Conclusiones

Se logró implementar un sistema capaz de generar figuras en un osciloscopio en modo XY mediante el uso del ESP32 y sus salidas DAC.

El uso de coordenadas permitió controlar con precisión la trayectoria del haz, evidenciando la relación entre señales eléctricas y representación gráfica.

Se comprobó que la velocidad de actualización influye directamente en la calidad de la imagen, siendo necesario ajustar los tiempos para lograr estabilidad.

La simulación con Arduino UNO permitió validar el comportamiento general del sistema, aunque con limitaciones debido al uso de PWM en lugar de señales analógicas reales.

Finalmente, la implementación en hardware real con ESP32 ofreció mejores resultados en precisión, estabilidad y calidad de la señal.

---
