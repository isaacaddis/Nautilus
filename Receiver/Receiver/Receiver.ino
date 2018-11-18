#include "Servo.h"

char sendsig[25]; //Initialized variable to store recieved data


Servo OutputM1;
Servo OutputM2;
Servo OutputM3;
Servo OutputM4;
Servo OutputM5;
Servo OutputM6;

void setup() {
  // Begin the Serial at 9600 Baud
  Serial.begin(9600);
  OutputM1.attach(10);
  OutputM2.attach(11);
  OutputM3.attach(12);
  OutputM4.attach(5);
  OutputM5.attach(3);
  OutputM6.attach(4);
}

void loop() {

  Serial.readBytes(sendsig,25); 
  String myString = String(sendsig);
  
  String mario = myString.substring(7,9);
  String luigi = myString.substring(10,12);
  String zerO = "0";

  if (myString.charAt(0) == '-') {
    Serial.println("L" + mario);
  }
  if (myString.charAt(0) == '+') {
    Serial.println("R" + mario);
  }
  if (myString.charAt(3) == '+') {
    Serial.println("F" + luigi);
  }
  if (myString.charAt(3) == '-') {
    Serial.println("B" + luigi);
  }
  if ((myString.charAt(0) == '0') && (myString.charAt(3) == '0')){
    Serial.println("N" + zerO);
    }
//
//    
//   Serial.println(taco1);

  delay(100);
}
