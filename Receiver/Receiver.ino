#include "Servo.h"

char joy[30];
  
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




String speedSeven;
String speedEight;


String speedNine;
String speedTen;

boolean twoMotors;
boolean fourMotors;



void setup() {
  Serial.begin(57600);
  //Serial.begin(57600);
  twoMotors = false;
  fourMotors = false;
  pinMode(LED_BUILTIN, OUTPUT);

  OutputM1.attach(10);
  OutputM2.attach(5);
  OutputM3.attach(3);
  OutputM4.attach(4);
  OutputM5.attach(11);
  OutputM6.attach(12);
  
  OutputM1.writeMicroseconds(1500);
  OutputM2.writeMicroseconds(1500);
  OutputM3.writeMicroseconds(1500);
  OutputM4.writeMicroseconds(1500);  
  OutputM5.writeMicroseconds(1500);
  OutputM6.writeMicroseconds(1500);

    speed01 = 1500;
    speed02 = 1500;
    speed03 = 1500;
    speed04 = 1500;
    speed05 = 1500;
    speed06 = 1500;
    speed07 = 1500;
    speed08 = 1500;
    speed09 = 1500;
    speed10 = 1500;
   
}

void loop() {

  Serial.readBytes(joy,30);
  Joystick = String(joy);
  
  SideSpeed = Joystick.substring((Joystick.indexOf("R") + 1), Joystick.indexOf("F"));
  FBSpeed = Joystick.substring((Joystick.indexOf("F") + 1), Joystick.indexOf("U"));
  VertSpeed = Joystick.substring((Joystick.indexOf("U") + 1), Joystick.indexOf("T"));
  TurnSpeed = Joystick.substring((Joystick.indexOf("T") + 1), Joystick.indexOf("P"));
  TiltSpeed = Joystick.substring((Joystick.indexOf("P") + 1), Joystick.length());

    fbSpeed = FBSpeed.toInt();
  sideSpeed = SideSpeed.toInt();
  vertSpeed = VertSpeed.toInt();
  turnSpeed = TurnSpeed.toInt();
  tiltSpeed = TiltSpeed.toInt();


   Serial.println(fbSpeed);
   Serial.println(sideSpeed);
   Serial.println(vertSpeed);
   Serial.println(turnSpeed);
   Serial.println(tiltSpeed);
   Serial.println("|||||");


   if((fbSpeed == 0) and (sideSpeed == 0) and (turnSpeed == 0)){
      fourMotors = false;
      OutputM1.writeMicroseconds(1500);
      OutputM2.writeMicroseconds(1500);
      OutputM3.writeMicroseconds(1500);
      OutputM4.writeMicroseconds(1500);

    }
    
   if( ((vertSpeed == 0) and (tiltSpeed == 0))){
      twoMotors = false;
      OutputM5.writeMicroseconds(1500);
      OutputM6.writeMicroseconds(1500);
   }
    
    

   if (vertSpeed > 0) { //Up  
       
       if (fourMotors == true){
          speed08= map( vertSpeed, 0, 25, 1500, 1315);
          OutputM5.writeMicroseconds(speed08);
          OutputM6.writeMicroseconds(speed08);
        }
        
        if(fourMotors == false){
            speed08= map( vertSpeed, 0, 25, 1500, 1198);
            OutputM5.writeMicroseconds(speed08);
            OutputM6.writeMicroseconds(speed08);
        }
        
        twoMotors = true;


  }
        
  if (vertSpeed < 0) { //Down     
     
     vertSpeed = abs(vertSpeed);
  
      if (fourMotors == true){
          speed08= map( vertSpeed, 0, 25, 1500, 1682);
          OutputM5.writeMicroseconds(speed08);
          OutputM6.writeMicroseconds(speed08);
      }
      
      if(fourMotors ==false){
          speed10 = map(vertSpeed,0, 25, 1500, 1795);
          OutputM5.writeMicroseconds(speed10);
          OutputM6.writeMicroseconds(speed10);
      }
    
    twoMotors = true;


    
  }

   if (tiltSpeed > 0) { //Tilt Up
       if(fourMotors == false){  
            speed05 = map( tiltSpeed, 0, 25, 1500, 1795);
            speed06 = map( speed05, 1500, 1795, 1500, 1198);
            OutputM5.writeMicroseconds(speed06);
            OutputM6.writeMicroseconds(speed05);
        }
        
        if(fourMotors == true){
            speed05 = map( tiltSpeed, 0, 25, 1500, 1682);
            speed06 = map( speed05, 1500, 1682, 1500, 1315);
            OutputM5.writeMicroseconds(speed06);
            OutputM6.writeMicroseconds(speed05);
        }
        
        twoMotors = true;

  }
        
  if (tiltSpeed < 0) { //Tilt Down
    tiltSpeed = abs(tiltSpeed);
       
       if(fourMotors == false){
            speed05 = map( tiltSpeed, 0, 25, 1500, 1795);
            speed06 = map( speed05, 1500, 1795, 1500, 1198);
            OutputM5.writeMicroseconds(speed05);
            OutputM6.writeMicroseconds(speed06);
        }
        
       if(fourMotors == true){
            speed05 = map( tiltSpeed, 0, 25, 1500, 1682);
            speed06 = map( speed05, 1500, 1682, 1500, 1315);
            OutputM5.writeMicroseconds(speed05);
            OutputM6.writeMicroseconds(speed06);
       }
    twoMotors = true;
  }



   if (fbSpeed > 0) { //Forwards
       
       if(twoMotors == false){
    
          speed07 = map(fbSpeed, 0, 25, 1500, 1198);
          OutputM1.writeMicroseconds(speed07);
          OutputM2.writeMicroseconds(speed07);
          OutputM3.writeMicroseconds(speed07);
          OutputM4.writeMicroseconds(speed07);
       }
       
       if(twoMotors == true){
          speed07 = map(fbSpeed, 0, 25, 1500, 1315);
          OutputM1.writeMicroseconds(speed07);
          OutputM2.writeMicroseconds(speed07);
          OutputM3.writeMicroseconds(speed07);
          OutputM4.writeMicroseconds(speed07);
       
       }
       
       fourMotors = true;

  }
  if (fbSpeed < 0) { //Backwards
    fbSpeed = abs(fbSpeed);
    
      if(twoMotors == false){
          speed09 = map(fbSpeed, 0, 25, 1500, 1795);
          OutputM1.writeMicroseconds(speed09);
          OutputM2.writeMicroseconds(speed09);
          OutputM3.writeMicroseconds(speed09);
          OutputM4.writeMicroseconds(speed09);
     }
     
     if(twoMotors == true){
          speed09 = map(fbSpeed, 0, 25, 1500, 1682);
          OutputM1.writeMicroseconds(speed09);
          OutputM2.writeMicroseconds(speed09);
          OutputM3.writeMicroseconds(speed09);
          OutputM4.writeMicroseconds(speed09);   
     }
     
     fourMotors = true;

  }
 if (sideSpeed > 0) { //Right 
 
    if(twoMotors == false){
    
        speed01 = map(sideSpeed, 0, 25, 1500, 1795);
        speed02 = map(sideSpeed, 0, 25, 1500, 1198);
        OutputM1.writeMicroseconds(speed02);
        OutputM2.writeMicroseconds(speed01);
        OutputM3.writeMicroseconds(speed01);
        OutputM4.writeMicroseconds(speed02);
    }
    
    if(twoMotors == true){
    
        speed01 = map(sideSpeed, 0, 25, 1500, 1682);
        speed02 = map(sideSpeed, 0, 25, 1500, 1315);
        OutputM1.writeMicroseconds(speed02);
        OutputM2.writeMicroseconds(speed01);
        OutputM3.writeMicroseconds(speed01);
        OutputM4.writeMicroseconds(speed02);
    }
    
    fourMotors = true;

    
  }

   if (sideSpeed < 0) { // Left
    sideSpeed = abs(sideSpeed);
    
    if(twoMotors == false){
    
    speed01 = map(sideSpeed, 0, 25, 1500, 1795);
    speed02 = map(sideSpeed, 0, 25, 1500, 1198);
    OutputM1.writeMicroseconds(speed01);
    OutputM2.writeMicroseconds(speed02);
    OutputM3.writeMicroseconds(speed02);
    OutputM4.writeMicroseconds(speed01);
    }
    
    if (twoMotors == true){
        speed01 = map(sideSpeed, 0, 25, 1500, 1682);
        speed02 = map(sideSpeed, 0, 25, 1500, 1315);
        OutputM1.writeMicroseconds(speed01);
        OutputM2.writeMicroseconds(speed02);
        OutputM3.writeMicroseconds(speed02);
        OutputM4.writeMicroseconds(speed01);
    }
    
    fourMotors = true;
    

  }
  
  
    if (turnSpeed > 0) { //Turn Clock Wise ( turn Right)
    
    if(twoMotors == false){
    
        speed03 = map(turnSpeed, 0, 25, 1500, 1795);
        speed04 = map(turnSpeed, 0, 25, 1500, 1198);
        OutputM1.writeMicroseconds(speed04);
        OutputM2.writeMicroseconds(speed03);
        OutputM3.writeMicroseconds(speed04);
        OutputM4.writeMicroseconds(speed03);
    }
    
    if(twoMotors == true){
    
        speed03 = map(turnSpeed, 0, 25, 1500, 1682);
        speed04 = map(turnSpeed, 0, 25, 1500, 1315);
        OutputM1.writeMicroseconds(speed04);
        OutputM2.writeMicroseconds(speed03);
        OutputM3.writeMicroseconds(speed04);
        OutputM4.writeMicroseconds(speed03);
    }
    
    fourMotors = true;

  }
  if (turnSpeed <0) { //Turn Counter ClockwIse ( Turn Left)
    turnSpeed = abs(turnSpeed);
    
    if(twoMotors == false){
    
        speed03 = map(turnSpeed, 0, 25, 1500, 1795);
        speed04 = map(turnSpeed, 0, 25, 1500, 1198);
        OutputM1.writeMicroseconds(speed03);
        OutputM2.writeMicroseconds(speed04);
        OutputM3.writeMicroseconds(speed03);
        OutputM4.writeMicroseconds(speed04);
    }
    
    if(twoMotors == true){
    
        speed03 = map(turnSpeed, 0, 25, 1500, 1682);
        speed04 = map(turnSpeed, 0, 25, 1500, 1315);
        OutputM1.writeMicroseconds(speed03);
        OutputM2.writeMicroseconds(speed04);
        OutputM3.writeMicroseconds(speed03);
        OutputM4.writeMicroseconds(speed04);
    }
    
    fourMotors = true;


  }
  
  if ((fbSpeed == 0) and (sideSpeed == 0) and (vertSpeed  == 0)  and (turnSpeed == 0)  and (tiltSpeed == 0) ){

    OutputM1.writeMicroseconds(1500);
    OutputM2.writeMicroseconds(1500);
    OutputM3.writeMicroseconds(1500);
    OutputM4.writeMicroseconds(1500);  
    OutputM5.writeMicroseconds(1500);
    OutputM6.writeMicroseconds(1500); 
    speed01 = 1500;
    speed02 = 1500;
    speed03 = 1500;
    speed04 = 1500;
    speed05 = 1500;
    speed06 = 1500;
    speed07 = 1500;
    speed08 = 1500;
    speed09 = 1500;
    speed10 = 1500;
   }  
    
  }