// Código de prueba mínimo - SOLO para probar comunicación serial
void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  
  // Apagar LEDs
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  
  Serial.println("INICIADO"); // Mensaje de confirmación
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();  // Leer un solo carácter
    
    if (c == 'R') {
      digitalWrite(9, HIGH);
      digitalWrite(10, LOW);
      Serial.println("ROJO");
    }
    else if (c == 'G') {
      digitalWrite(9, LOW);
      digitalWrite(10, HIGH);
      Serial.println("VERDE");
    }
  }
}