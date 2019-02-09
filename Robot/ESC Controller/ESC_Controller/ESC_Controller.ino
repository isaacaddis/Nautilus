/**
 * @author Jiajer Ho and Alexander Vazquez
 * 
 * ROV ESC Controller Underwater Code (Receiver)  08/03/2018
 * Use ATMEGA1260 or 2560
 * 
 * Takes data from Surface Arduino and determine the ESC control  
 * 
 *
 
 #include "Servo.h"

char sendsig[25]; //Initialized variable to store recieved data

int speed01; 
int speed02; 
int speed03; 
int luigiInt;
Servo OutputM1; //Motor 1 FRD/BCK AND PLFT/PRGT AND LFT/RGT
Servo OutputM2; //Motor 2 FRD/BCK AND PLFT/PRGT AND LFT/RGT
Servo OutputM3; //Motor 3 FRD/BCK AND PLFT/PRGT AND LFT/RGT
Servo OutputM4; //Motor 4 FRD/BCK AND PLFT/PRGT AND LFT/RGT
Servo OutputM5; //Motor 5 UP/DOWN AND TILT
Servo OutputM6; //Motor 6 UP/DOWN AND TILT

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
  int luigiInt = luigi.toInt();
 
  
  if (myString.charAt(0) == '-') { //PLeft
    Serial.println("L" + mario);
    speed01 = map(luigiInt, 1, 10, 90, 180);
    speed02 = map(luigiInt, 1, 10, 90, 0);
    OutputM1.write(speed01);
    OutputM2.write(speed02);
    OutputM3.write(speed02);
    OutputM4.write(speed01);
  }
  if (myString.charAt(0) == '+') { //PRight
    Serial.println("R" + mario);
    speed01 = map(luigiInt, 1, 10, 90, 180);
    speed02 = map(luigiInt, 1, 10, 90, 0);
    OutputM1.write(speed02);
    OutputM2.write(speed01);
    OutputM3.write(speed01);
    OutputM4.write(speed02);
  }
  if (myString.charAt(3) == '+') { //Forwards
    Serial.println("F" + luigi);
    speed01 = map(luigiInt, 1, 10, 90, 0);
    OutputM1.write(speed01);
    OutputM2.write(speed01);
    OutputM3.write(speed01);
    OutputM4.write(speed01);
  }
  if (myString.charAt(3) == '-') { //Backwards
    Serial.println("B" + luigi);
    speed01 = map(luigiInt, 1, 10, 90, 180);
    OutputM1.write(speed01);
    OutputM2.write(speed01);
    OutputM3.write(speed01);
    OutputM4.write(speed01);
  }
  if ((myString.charAt(0) == '0') && (myString.charAt(3) == '0')){
    Serial.println("N" + zerO);
    OutputM1.write(90);
    OutputM2.write(90);
    OutputM3.write(90);
    OutputM4.write(90);
    }
    
   delay(100);
}/
