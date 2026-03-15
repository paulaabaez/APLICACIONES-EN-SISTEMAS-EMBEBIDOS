char dato;

void setup(){

Serial.begin(9600);

pinMode(7,OUTPUT);
pinMode(8,OUTPUT);
pinMode(9,OUTPUT);
pinMode(10,OUTPUT);

}

void loop(){

if(Serial.available()){

dato = Serial.read();

digitalWrite(7,LOW);
digitalWrite(8,LOW);
digitalWrite(9,LOW);
digitalWrite(10,LOW);

if(dato=='C'){   // circulo rojo
digitalWrite(7,HIGH);
digitalWrite(8,HIGH);
}

if(dato=='R'){   // rectangulo verde
digitalWrite(7,HIGH);
digitalWrite(9,HIGH);
}

if(dato=='S'){   // cuadrado azul
digitalWrite(7,HIGH);
digitalWrite(10,HIGH);
}

}

}