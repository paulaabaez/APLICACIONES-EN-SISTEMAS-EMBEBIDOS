# Sistema de Detección de Colores con Arduino y OpenCV

Proyecto de laboratorio que integra visión por computadora usando OpenCV con control de hardware mediante Arduino Uno.

La cámara detecta objetos de color rojo, verde o azul y envía un comando al Arduino para encender LEDs indicadores.

---

# Tecnologías utilizadas

- Python  
- OpenCV  
- Comunicación Serial (PySerial)  
- Arduino Uno  

---

# Funcionamiento del sistema

El flujo del sistema es:

```
Cámara → OpenCV detecta color → Python envía comando → Arduino enciende LEDs
```

Cuando el sistema detecta un color:

| Color detectado | Comando enviado | LED encendido |
|---|---|---|
| Rojo | R | LED rojo |
| Verde | G | LED verde |
| Azul | B | LED azul |

---

# Versión 1 del sistema

## Características

- Detecta colores usando OpenCV
- Enciende LEDs según el color detectado
- Dibuja un rectángulo alrededor del objeto detectado

## Comportamiento

En esta versión:

- No se mostraba información en la terminal
- Los LEDs permanecían encendidos incluso si el objeto desaparecía
- Los LEDs solo cambiaban si se mostraba un objeto de otro color

### Ejemplo de comportamiento

```
Objeto rojo detectado → LED rojo encendido

Se retira el objeto → LED rojo sigue encendido

Objeto azul detectado → LED azul cambia al nuevo color
```

Esto ocurría porque el sistema no enviaba ningún comando cuando no detectaba objetos.

---

# Versión 2 del sistema (Mejorada)

## Mejoras implementadas

Se agregó una mejora en la comunicación entre Python y Arduino:

```
'N' = No hay objeto detectado
```

Ahora el sistema puede apagar los LEDs automáticamente cuando no hay detección.

## Nuevas características

- Muestra información en la terminal
- Apaga LEDs cuando no hay objeto
- Mantiene detección en tiempo real
- Sigue mostrando recuadro del objeto detectado

---

## Ejemplo de salida en la terminal

Cuando se detecta un objeto:

```
Detectado: ROJO
```

Cuando no hay objeto:

```
Sin objeto
```

---

# Comportamiento del sistema mejorado

| Situación | Resultado |
|---|---|
| Se detecta objeto rojo | LED estado + LED rojo |
| Se detecta objeto verde | LED estado + LED verde |
| Se detecta objeto azul | LED estado + LED azul |
| No hay objeto | Todos los LEDs apagados |

---

# Visualización en la cámara

El sistema también muestra en la cámara:

- Rectángulo alrededor del objeto detectado
- Nombre del color detectado

Ejemplo:

```
┌───────────────┐
│               │
│     ROJO      │
│               │
└───────────────┘
```

---

# Conclusión

La segunda versión mejora significativamente el sistema al:

- Proporcionar retroalimentación en la terminal
- Apagar automáticamente los LEDs cuando no hay detección
- Mantener una interacción más clara entre software y hardware

Esto hace que el sistema sea más robusto y adecuado para demostraciones de laboratorio.
