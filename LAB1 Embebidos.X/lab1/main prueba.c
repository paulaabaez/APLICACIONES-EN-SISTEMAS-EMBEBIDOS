#include <xc.h>

// CONFIGURACIÓN (cristal externo HS)
#pragma config FOSC = HS
#pragma config WDTE = OFF
#pragma config PWRTE = ON
#pragma config MCLRE = ON
#pragma config CP = OFF
#pragma config CPD = OFF
#pragma config BOREN = ON
#pragma config IESO = OFF
#pragma config FCMEN = OFF
#pragma config LVP = OFF

#define _XTAL_FREQ 8000000  // 8 MHz

// Tabla para display 7 segmentos cátodo común
// Orden bits: gfedcba
const unsigned char tabla[16] = {
    0x3F, // 0
    0x06, // 1
    0x5B, // 2
    0x4F, // 3
    0x66, // 4
    0x6D, // 5
    0x7D, // 6
    0x07, // 7
    0x7F, // 8
    0x6F, // 9
    0x77, // A
    0x7C, // b
    0x39, // C
    0x5E, // d
    0x79, // E
    0x71  // F
};

void main() {
    
    // Desactivar entradas analógicas
    ANSEL = 0x00;
    ANSELH = 0x00;
    
    // Configurar puertos
    TRISA = 0x0F;   // RA0-RA3 entradas
    TRISB = 0x00;   // PORTB salidas
    
    PORTB = 0x00;

    while(1) {
        
        unsigned char valor;
        
        valor = PORTA & 0x0F;  // Leer solo RA0-RA3
        
        PORTB = tabla[valor];  // Mostrar en display
        
        __delay_ms(100);
    }
}
