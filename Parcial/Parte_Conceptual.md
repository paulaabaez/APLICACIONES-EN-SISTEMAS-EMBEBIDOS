# Parte Conceptual - Respuestas a Preguntas

## 1.1 Microcontroladores vs Microprocesadores

| | Microcontrolador | Microprocesador |
|---|---|---|
| **Definición** | Chip que contiene todo su sistema en un solo integrado (CPU, RAM, ROM, periféricos) | Dispositivo diseñado para ejecutar instrucciones y procesar datos |
| **Componentes** | Todo integrado en el chip | Solo CPU, requiere componentes externos |
| **Aplicación** | Control de sistemas embebidos, dispositivos autónomos | Computadoras personales, servidores |
| **Consumo** | Bajo (optimizado para autonomía) | Alto |
| **Ejemplos** | Arduino, PIC, ESP32 | Intel Core, AMD Ryzen |

---

## 1.2 Arquitecturas Von Neumann y Harvard

### Von Neumann
| Aspecto | Descripción |
|--------|-------------|
| **Característica principal** | Único espacio de memoria y un solo bus para instrucciones y datos |
| **Ventaja** | Diseño simple y económico de implementar |
| **Desventaja** | Cuello de botella: la CPU debe esperar si el bus está ocupado |
| **Acceso** | No puede leer instrucción y dato al mismo tiempo |

### Harvard
| Aspecto | Descripción |
|--------|-------------|
| **Característica principal** | Dos espacios de memoria y buses separados (programa y datos) |
| **Ventaja** | Acceso simultáneo a instrucción y dato, ideal para tiempo real |
| **Desventaja** | Hardware más complejo |

---

## 1.3 Procesadores RISC vs CISC

| Característica | CISC | RISC |
|---|---|---|
| **Instrucciones** | Complejas y potentes | Simples, reducidas y optimizadas |
| **Ciclos por instrucción** | Múltiples operaciones de bajo nivel | Un solo ciclo de reloj |
| **Objetivo** | Reducir tamaño del código | Simplificar hardware, mayor velocidad y eficiencia |
| **Hardware** | Complejo | Sencillo |
| **Ejemplos** | Intel x86, AMD64 | ARM, RISC-V |

---

## 1.4 ARM (Advanced RISC Machine)

**Definición:** Familia de arquitecturas de procesadores de tipo RISC de 32 y 64 bits. A diferencia de Intel o AMD, **ARM Holdings no fabrica chips**, sino que **diseña la arquitectura y la licencia** a otras empresas.

### Características
| Aspecto | Descripción |
|--------|-------------|
| **Versatilidad** | Existen diferentes versiones para distintos propósitos |
| **Cortex-A** | Alto rendimiento para smartphones |
| **Cortex-R** | Tiempo real |
| **Cortex-M** | Ultra bajo consumo para IoT |
| **Personalización** | Modelo de licencias permite adaptar diseños |

### Ventajas
-  Excelente relación **rendimiento por vatio**
-  Ideal para dispositivos con batería

### Uso actual
**Sí, es muy usado:**
-  99% de los smartphones funcionan con ARM
-  Portátiles Apple Silicon (M1, M2, M3)
-  Servidores en la nube (AWS Graviton)
-  Supercomputadoras

---

## 1.5 Arquitectura de Arduino

**Arduino no es un microcontrolador**, es una **plataforma de desarrollo de hardware y software libre**.

### Arquitectura
| Placa | Arquitectura |
|-------|--------------|
| Arduino Uno (clásica) | Microcontroladores AVR de 8 bits (Atmel/Microchip) |
| | Basada en **Harvard modificada** + núcleo **RISC** |
| Arduino Due (moderno) | ARM de 32 bits |

### Características principales
| Característica | Descripción |
|----------------|-------------|
| **Bootloader** | Permite cargar código (Sketch) vía USB sin programador externo |
| **Hardware Abierto** | Esquemáticos y diseños públicos, permite crear versiones propias |
| **Pines de E/S** | Digitales (algunos con PWM) y analógicos (ADC) |
| **IDE Simple** | Basado en Processing/Wiring, accesible para principiantes |
| **Comunicación** | UART (serie), I2C, SPI |

---

## 1.6 Arquitectura del PIC16F887

**Microcontrolador de 8 bits** de Microchip Technology.

### Arquitectura
| Aspecto | Descripción |
|--------|-------------|
| **Tipo** | 8 bits |
| **Arquitectura** | Harvard (buses y memorias separadas) |
| **Núcleo** | RISC |

### Características principales
| Componente | Especificación |
|------------|----------------|
| **Instrucciones** | 35 instrucciones (una palabra cada una) |
| **Velocidad** | Hasta 20 MHz |

### Memorias
| Tipo | Capacidad |
|------|-----------|
| Flash (programa) | 8 KB (reprogramable) |
| RAM (datos temporales) | 368 bytes |
| EEPROM (datos no volátiles) | 256 bytes |

### Periféricos integrados
| Periférico | Cantidad/Especificación |
|------------|-------------------------|
| Pines E/S | 35 (multifunción) |
| Módulos CCP | 2 (Captura/Comparación/PWM) |
| Convertidor A/D | 14 canales, 10 bits |
| Comparadores analógicos | 2 |
| Temporizadores | 3 (2 de 8 bits, 1 de 16 bits) |
| Comunicación | USART, SPI, I2C |

---

##  Resumen de diferencias clave

| Concepto | Diferencia principal |
|----------|----------------------|
| Microcontrolador vs Microprocesador | Todo en uno vs solo CPU |
| Von Neumann vs Harvard | Un bus vs dos buses |
| RISC vs CISC | Instrucciones simples vs complejas |
| ARM | Arquitectura licenciable, eficiencia energética |
| Arduino | Plataforma, no chip (AVR o ARM) |
| PIC16F887 | 8 bits, Harvard, RISC, 35 instrucciones |


