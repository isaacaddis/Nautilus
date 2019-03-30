#include "Servo.h"

char joy[25];
  
String  FBSpeed;
String SideSpeed;
String VertSpeed; 
String TurnSpeed; 
String TiltSpeed; 

int  fbSpeed;
int sideSpeed;
int vertSpeed; 
int turnSpeed; 
int tiltSpeed; 


String Joystick;
String message; 

Servo OutputM1;
Servo OutputM2;
Servo OutputM3;
Servo OutputM4;
Servo OutputM5;
Servo OutputM6;


int speed01;
int speed02;

int speed03;
int speed04;


int speed05;
int speed06;

int speed07;
int speed08;


int speed09;
int speed10;



String speedOne;
String speedTwo;

String speedThree;
String speedFour;


String speedFive;
String speedSix;

String speedSeven;
String speedEight;


String speedNine;
String speedTen;



void setup() {
  Serial.begin(57600);
  Serial1.begin(57600);
  Serial2.begin(57600);
  pinMode(LED_BUILTIN, OUTPUT);

  OutputM1.attach(10);
  OutputM2.attach(5);
  OutputM3.attach(3);
  OutputM4.attach(4);
  OutputM5.attach(11);
  OutputM6.attach(12);
  
  OutputM1.write(90);
  OutputM2.write(90);
  OutputM3.write(90);
  OutputM4.write(90);  
  OutputM5.write(90);
  OutputM6.write(90); 
  
  delay(500);
  // put your setup code here, to run once:

}

void loop() {
  Serial1.readBytes(joy,25);
  Joystick = String(joy);
  //Serial.println(Joystick);
 // Serial.println(Joystick);
  //digitalWrite(LED_BUILTIN, HIGH);
  
  FBSpeed = Joystick.substring((Joystick.indexOf("R") + 1), Joystick.indexOf("F"));
  SideSpeed = Joystick.substring((Joystick.indexOf("F") + 1), Joystick.indexOf("U"));
  VertSpeed = Joystick.substring((Joystick.indexOf("U") + 1), Joystick.indexOf("T"));
  TurnSpeed = Joystick.substring((Joystick.indexOf("T") + 1), Joystick.indexOf("P"));
  TiltSpeed = Joystick.substring((Joystick.indexOf("P") + 1), Joystick.length());

    fbSpeed = FBSpeed.toInt();
  sideSpeed = SideSpeed.toInt();
  vertSpeed = VertSpeed.toInt();
  turnSpeed = TurnSpeed.toInt();
  tiltSpeed = TiltSpeed.toInt() ;


 //  Serial.println(fbSpeed);
 //  Serial.println(sideSpeed);
 //  Serial.println(vertSpeed);
 //  Serial.println(turnSpeed);
 //  Serial.println(tiltSpeed);


   if (vertSpeed > 0) { //Up    
    speed08= map( vertSpeed, 0, 25, 90, 0);
    OutputM5.write(speed08);
    OutputM6.write(speed08);
//    speedEight = String(speed08);
//    Serial2.println("Up"+ speedEight);
  }
        
  if (vertSpeed < 0) { //Down 
    vertSpeed = abs(vertSpeed);
    speed10 = map(vertSpeed,0, 25, 90, 180);
    OutputM5.write(speed10);
    OutputM6.write(speed10);
//    speedTen = String(speed10);
//    Serial2.println("Vertical"+ speedTen);
    
  }

   if (tiltSpeed > 0) { //Tilt Up
    speed05 = map( tiltSpeed, 0, 25, 90, 180);
    speed06 = map( tiltSpeed, 0, 25, 0, 90);
    OutputM5.write(speed06);
    OutputM6.write(speed05);
//    speedSix = String(speed06);
//    speedFive = String(speed05);
//    Serial2.println("Tilt Up" +speedSix);
//    Serial2.println("Tilt Up" + speedFive);
  }
        
  if (tiltSpeed < 0) { //Tilt Down
    tiltSpeed = abs(tiltSpeed);
    speed05 = map( tiltSpeed, 0, 25, 90, 180);
    speed06 = map( tiltSpeed, 0, 25, 0, 90);
    OutputM5.write(speed05);
    OutputM6.write(speed06);
//    speedSix = String(speed06);
//    speedFive = String(speed05);
//    Serial2.println("Tilt Down" +speedSix);
//    Serial2.println("Tilt Down" + speedFive);
  }



   if (fbSpeed > 0) { //Forwards
    speed07 = map(fbSpeed, 0, 25, 90, 0);
    OutputM1.write(speed07);
    OutputM2.write(speed07);
    OutputM3.write(speed07);
    OutputM4.write(speed07);
//    speedSeven = String(speed07);
//    Serial2.println("Forward"+speedSeven);
  }
  if (fbSpeed < 0) { //Backwards
    fbSpeed = abs(fbSpeed);
    speed09 = map(fbSpeed, 0, 25, 90, 180);
    OutputM1.write(speed09);
    OutputM2.write(speed09);
    OutputM3.write(speed09);
    OutputM4.write(speed09);
//    speedNine = String(speed09);
//    Serial2.println("Forward"+speedNine);
  }
 if (sideSpeed > 0) { //Right 
    speed01 = map(turnSpeed, 0, 25, 90, 180);
    speed02 = map(turnSpeed, 0, 25, 90, 0);
    OutputM1.write(speed02);
    OutputM2.write(speed01);
    OutputM3.write(speed01);
    OutputM4.write(speed02);
//    speedOne = String(speed01);
//    speedTwo = String(speed01);
//    Serial2.println("Right"+ speedOne);
//    Serial2.println("Right" + speedTwo);
    
  }

   if (sideSpeed < 0) { // Left
    sideSpeed = abs(sideSpeed);
    speed01 = map(turnSpeed, 0, 25, 90, 180);
    speed02 = map(turnSpeed, 0, 25, 90, 0);
    OutputM1.write(speed01);
    OutputM2.write(speed02);
    OutputM3.write(speed02);
//    OutputM4.write(speed01);
//    speedOne = String(speed01);
//    speedTwo = String(speed01);
//    Serial2.println("Left"+ speedOne);
//    Serial2.println("Left" + speedTwo);
  }
    if (turnSpeed > 0) { //Turn Clock Wise ( turn Right)
    speed03 = map(turnSpeed, 0, 25, 90, 180);
    speed04 = map(turnSpeed, 0, 25, 90, 0);
    OutputM1.write(speed04);
    OutputM2.write(speed03);
    OutputM3.write(speed04);
    OutputM4.write(speed03);
//    speedThree = String(speed04);
//    speedFour = String(speed03);
//    Serial2.println("Turn Right"+ speedThree);
//    Serial2.println("Turn Right" + speedFour);
  }
  if (turnSpeed <0) { //Turn Counter ClockwIse ( Turn Left)
    turnSpeed = abs(turnSpeed);
    speed03 = map(turnSpeed, 0, 25, 90, 180);
    speed04 = map(turnSpeed, 0, 25, 90, 0);
    OutputM1.write(speed03);
    OutputM2.write(speed04);
    OutputM3.write(speed03);
    OutputM4.write(speed04);
//    speedThree = String(speed03);
//    speedFour = String(speed04);
//    Serial2.println("Turn Left"+ speedThree);
//    Serial2.println("Turn Left" + speedFour);
  }
  
  if ((fbSpeed == 0) and (sideSpeed == 0) and (vertSpeed  == 0)  and (turnSpeed == 0)  and (tiltSpeed == 0) ){

    OutputM1.write(90);
    OutputM2.write(90);
    OutputM3.write(90);
    OutputM4.write(90);  
    OutputM5.write(90);
    OutputM6.write(90); 
   }  
  delay(300);

  
    
  }