#include <xc.h>

// Bits de configuración para Cristal de 4MHz
#pragma config FOSC = XT, WDTE = OFF, LVP = OFF
#define _XTAL_FREQ 4000000

// Tabla para Ánodo Común (0-9 y A-F)
// Un '0' en el bit enciende el segmento, un '1' lo apaga.
unsigned char const table[] = {
    0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xF8, 0x80, 0x90, // 0-9
    0x88, 0x83, 0xC6, 0xA1, 0x86, 0x8E                          // A-F
};

unsigned char modo = 0; // 0: Decimal, 1: Octal, 2: Hexadecimal

void main(void) {
    ADCON1 = 0x06; // Configura todo el Puerto A como digital
    TRISB = 0xFF;  // Puerto B como entrada (DIP Switch de 8 bits)
    TRISA = 0x08;  // RA3 como entrada (Botón), RA0-RA2 como salidas (Displays)
    TRISD = 0x00;  // Puerto D como salida (Segmentos a-g)
    
    unsigned char valor, d1, d2, d3;

    while(1) {
        // --- Lógica del Botón Selector (RA3) ---
        if(PORTAbits.RA3 == 1) { 
            __delay_ms(50); // Antirrebote (Debounce)
            if(PORTAbits.RA3 == 1) {
                modo++;
                if(modo > 2) modo = 0; // Reinicia a Decimal después de Hex
                while(PORTAbits.RA3 == 1); // Espera a que sueltes el botón
            }
        }

        valor = PORTB; // Lee el byte del DIP Switch (0 a 255)

        // --- Cálculos según la Base Seleccionada ---
        if(modo == 0) { // BASE DECIMAL (10)
            d3 = valor / 100;         // Centenas
            d2 = (valor % 100) / 10;  // Decenas
            d1 = valor % 10;          // Unidades
        } 
        else if(modo == 1) { // BASE OCTAL (8)
            // El máximo 255 dec es 377 octal
            d3 = (valor / 64) % 8;    // Tercer dígito octal
            d2 = (valor / 8) % 8;     // Segundo dígito octal
            d1 = valor % 8;           // Primer dígito octal
        } 
        else { // BASE HEXADECIMAL (16)
            // El máximo 255 dec es FF hex
            d3 = 16; // Usamos el índice 16 para apagar el display (ver lógica abajo)
            d2 = valor / 16;          // Primer nibble (F_)
            d1 = valor % 16;          // Segundo nibble (_F)
        }

        // --- Rutina de Multiplexación (Displays Ánodo Común) ---
        
        // 1. Mostrar Dígito 1 (Derecha / Unidades)
        PORTD = table[d1];
        PORTAbits.RA0 = 1;  // Activa Ánodo del Display 1
        __delay_ms(5);
        PORTAbits.RA0 = 0;  // Apaga

        // 2. Mostrar Dígito 2 (Centro / Decenas)
        PORTD = table[d2];
        PORTAbits.RA1 = 1;  // Activa Ánodo del Display 2
        __delay_ms(5);
        PORTAbits.RA1 = 0;  // Apaga

        // 3. Mostrar Dígito 3 (Izquierda / Centenas)
        if(d3 < 10 || (modo == 1 && d3 < 8)) { // Solo muestra si es válido
            PORTD = table[d3];
            PORTAbits.RA2 = 1; // Activa Ánodo del Display 3
            __delay_ms(5);
            PORTAbits.RA2 = 0; // Apaga
        } else {
            // En Hexadecimal, d3 es 16, por lo que este display se queda apagado
            __delay_ms(5); 
        }
    }
}