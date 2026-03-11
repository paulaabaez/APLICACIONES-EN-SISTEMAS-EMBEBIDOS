#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

const int ledRojo = 8;
const int ledVerde = 9;

void setup() {

  pinMode(ledRojo, OUTPUT);
  pinMode(ledVerde, OUTPUT);

  Serial.begin(9600);
  dht.begin();
}

void loop() {

  if (Serial.available() > 0) {

    String comando = Serial.readStringUntil('\n');
    comando.trim();

    if (comando == "LED ROJO ON") {
      digitalWrite(ledRojo, HIGH);
      Serial.println("LED rojo encendido");
    }

    else if (comando == "LED ROJO OFF") {
      digitalWrite(ledRojo, LOW);
      Serial.println("LED rojo apagado");
    }

    else if (comando == "LED VERDE ON") {
      digitalWrite(ledVerde, HIGH);
      Serial.println("LED verde encendido");
    }

    else if (comando == "LED VERDE OFF") {
      digitalWrite(ledVerde, LOW);
      Serial.println("LED verde apagado");
    }

    else if (comando == "TEMPERATURA") {

      float temperatura = dht.readTemperature();

      if (isnan(temperatura)) {
        Serial.println("Error leyendo sensor");
      } 
      else {
        Serial.print("Temperatura: ");
        Serial.print(temperatura);
        Serial.println(" C");
      }
    }
  }
}
