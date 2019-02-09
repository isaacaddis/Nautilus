////Receiver Code
//
//char str[4];
//
//void setup() {
//  Serial.begin(9600);
//  Serial1.begin(9600);
//}
//
//void loop() {
//  int i=0;
//
//  if (Serial1.available()) {
//    delay(100); //allows all serial sent to be received together
//    while(Serial1.available() && i<4) {
//      str[i++] = Serial1.read();
//    }
//    str[i++]='\0';
//  }
//
// if(i>0) {
//    for(int j =0; j<4;j++) {
//        Serial.print(str[j]);
//    }
//    Serial.println("");
// }
//}

//Receiver Code


#include "Servo.h"


char sending[40]; //Initialized variable to store recieved data



int side_speed; // left right speed
int fb_speed; // forward backward speed
int vertcial_speed; // up  down speed
int turn_speed; // turning speed
int tilt_speed; // tilting speed
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
  Serial.readBytes(sending,40);
  Serial.println(sending);
  
  Serial.readBytes(sendsig,40); 
  String myString = String(sendsig);
 
  String for_back_speed = myString.substring( ,);
  String left_right_speed = myString.substring( , );
  String verticalSpeed = myString.substring( ,);
  String turningSpeed = myString.substring( , );
  String tiltSpeed = myString.substring(,);
  
  fb_speed = for_back_speed.toInt();
  side_speed = left_right_speed.toInt();
  vertcial_speed = verticalSpeed.toInt(); 
  turn_speed = turningSpeed.toInt(); 
  tilt_speed= tiltSpeed.toInt(); 
  
  

  
  if (myString.charAt(0) == '-') { //PLeft
    Serial.println("L" + mario);
    speed01 = map(marioInt, 1, 10, 90, 180);
    speed02 = map(marioInt, 1, 10, 90, 0);
    OutputM1.write(speed01);
    OutputM2.write(speed02);
    OutputM3.write(speed02);
    OutputM4.write(speed01);
  }
  if (myString.charAt(0) == '+') { //PRight
    Serial.println("R" + mario);
    speed01 = map(marioInt, 1, 10, 90, 180);
    speed02 = map(marioInt, 1, 10, 90, 0);
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
  if (myString.charAt(6) == '+') { //Up
    Serial.println("U" + yoshi);
    speed03 = map(yoshiInt, 1, 10, 90, 180);
    OutputM5.write(speed03);
    OutputM6.write(speed03);
  }
  if (myString.charAt(6) == '-') { //Down
    Serial.println("D" + yoshi);
    speed03 = map(yoshiInt, 1, 10, 90, 0);
    OutputM5.write(speed03);
    OutputM6.write(speed03);
  }
   if ((myString.charAt(6) == '0') && (myString.charAt(15) == '0')){
    Serial.println("N" + zerO);
    OutputM5.write(90);
    OutputM6.write(90);
  }

  delay(100);
}
