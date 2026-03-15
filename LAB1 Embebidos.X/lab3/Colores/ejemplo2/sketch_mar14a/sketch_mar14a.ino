char dato;

void setup() {

Serial.begin(9600);

pinMode(7,OUTPUT);
pinMode(8,OUTPUT);
pinMode(9,OUTPUT);
pinMode(10,OUTPUT);

}

void loop() {

if(Serial.available()){

dato = Serial.read();

digitalWrite(7,LOW);
digitalWrite(8,LOW);
digitalWrite(9,LOW);
digitalWrite(10,LOW);

if(dato=='R'){
Serial.println("Rojo detectado");
digitalWrite(7,HIGH);
digitalWrite(8,HIGH);
}

if(dato=='G'){
Serial.println("Verde detectado");
digitalWrite(7,HIGH);
digitalWrite(9,HIGH);
}

if(dato=='B'){
Serial.println("Azul detectado");
digitalWrite(7,HIGH);
digitalWrite(10,HIGH);
}

if(dato=='N'){
Serial.println("Sin objeto");
}

}

}