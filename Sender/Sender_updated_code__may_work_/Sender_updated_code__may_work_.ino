#include "Servo.h"

const int InputA0 = A0; // Forward and Backward
const int InputA1 = A1; // Left and Right
const int InputA2 = A4; // Up and down
const int InputA3 = A3; // Tilt 
const int InputA4 = A2;// Turning
const int InputA5 = A5; 

String temp_in;
String temp_out;
String humidity;
String leak;
String gyroX;
String gyroY;

int PotA0 = 0;       
int SpeedA0 = 0;
int PotA1 = 0;
int SpeedA1 = 0;
int PotA2 = 0;
int SpeedA2 = 0;
int PotA3 = 0;
int SpeedA3= 0;
int PotA4 = 0;
int SpeedA4= 0;
int rotate = 0;
int PotA5;


int outputValueX = 0;
int outputValueY = 0;
int outputValueZ = 0;
int outputValueT = 0;
int outputValueP= 0;

int n = 0;

int XDirection = 0;
int YDirection = 0;
int ZDirection = 0; 
int TDirection = 0;
int PDirection = 0;

int SpeedY = 0;
int SpeedX = 0;
int SpeedZ = 0; 
int SpeedT = 0;
int SpeedP = 0;


String str1;
String str2;
String str3;
String str4;
String str5;
String str6;

String strSpeedY;
String strSpeedX;
String strSpeedZ;
String strSpeedT; 
String strSpeedP;
String rotMeasure; 

String strDirectX;
String strDirectY;
String strDirectZ; 
String strDirectT;
String strDirectP; 

String ultimateStr;
char joy[30];
char m_str[45];
const int clawPin1 = 2;
const int clawPin2 = 3;

int buttonState1 = 0;
int buttonState2 = 0;

String Button1;
String Button2;

void setup() {


Serial.begin(57600);
Serial1.begin(57600);
pinMode(clawPin1, INPUT);
pinMode(clawPin2, INPUT);
//Serial1.begin(57600);
 delay(500);

}

void loop() {
  PotA0 = analogRead(InputA0);
  PotA1 = analogRead(InputA1);
  PotA2 = analogRead(InputA2);
  PotA3 = analogRead(InputA3);
  PotA4 = analogRead(InputA4);
  PotA5 = analogRead(InputA5);

  buttonState1 = digitalRead(clawPin1);
  buttonState2 = digitalRead(clawPin2);

  if (buttonState1 == HIGH){
    Button1 = "1";
  }
  if (buttonState1 == LOW){
    Button1 = "0";
  }
  if(buttonState2 == HIGH){
    Button2 = "1";
  }
  if(buttonState2 == LOW){
    Button2 = "0";
  }
  
  outputValueY = map(PotA0, 0, 1023, -25, 25);
  outputValueX = map(PotA1, 0, 1023, -25, 25);
  outputValueZ = map(PotA2, 0, 1023, -25, 25);
  outputValueT = map(PotA3, 0, 1023, -25, 25);
  outputValueP = map(PotA4, 0, 1023, -25, 25);
  rotate = map(PotA5, 0 ,1023, 0, 180);

  
  int x = outputValueX;
  int y = outputValueY; 
  int z = outputValueZ;
  int t = outputValueT;
  int p = outputValueP;

  if((x <= -5 and x >= -24) and (y <= abs(x) and y >= 0) and (y != 25)){
    XDirection = -1;
    YDirection = 0;
}
  
if( (x <= -5 and x >= -24) and (y >= x and y < 0) and (y != 25)){
    XDirection = -1;
    YDirection = 0;

}
  if((x == -25) and (abs(y) <= 24)){
    XDirection = -1;
    YDirection = 0;

}
       
  if( (x >= 5 and x <= 24) and (abs(y)<= x and y < 0) and (y != 25)){
    XDirection = 1;
    YDirection = 0;

  }
  
  if( (x >= 5 and x <= 24) and (y <= x and y >= 0) and (y != 25)){
    XDirection = 1;
    YDirection = 0;
  }
  if((x == 25) and ( abs(y) <= 24)){
    XDirection = 1;
    YDirection = 0;

  }

  if((x >= -24 and x <= -5) and (x >= 5 and x <= 24) and (y > 0 and y > abs(x))){
    YDirection = 1;
    XDirection = 0;
  }
  if(( abs(x) == 25 ) and (y == 25)){
    YDirection = 1;
    XDirection = 0;
  }
  if((x >= -3 and x <= 3) and (y >= 5)) {
    YDirection = 1;
    XDirection = 0;

  }
  
     if( (x >= -24 and x <= -5) and (x >= 5 and x <= 24) and ( y < 0 and y < (-1 * abs(x)))){
     YDirection = -1;
     XDirection = 0;
  }
  
  if( ( abs(x) == 25 ) and (y == -25 )){
     YDirection = -1;
     XDirection = 0;
  }
  
  if((x >= -3 and x <= 3) and y <= -5){
    YDirection = -1;
    XDirection = 0;
  }    

  if( (x < 5 and x > -5) and (y < 5 and y > -5) ){
    YDirection = 0;
    XDirection = 0;
}

   
  if(z >= 5){
     ZDirection = 1;
   }
    if(z <= -5){
     ZDirection = -1;
   }
    if ((z< 5) and (z> -5) ) {
       ZDirection = 0;
   }
   
//Serial.println(z); 
  if((p <= -5 and p >= -24) and (t <= abs(p) and t >= 0) and (t != 25)){
    PDirection = -1;
    TDirection = 0;
}
  
if( (p <= -5 and p >= -24) and (t >= p and t < 0) and (t != 25)){
    PDirection = -1;
    TDirection = 0;

}
  if((p == -25) and (abs(t) <= 24)){
    PDirection = -1;
    TDirection = 0;
}
       
  if( (p >= 5 and p <= 24) and (abs(t)<= p and t < 0) and (t != 25)){
    PDirection = 1;
    TDirection = 0;
  }
  
  if( (p >= 5 and p <= 24) and (t <= p and t >= 0) and (t != 25)){
    PDirection = 1;
    TDirection = 0;
  }
  if((p == 25) and ( abs(t) <= 24)){
    PDirection = 1;
    TDirection = 0;
  }

 
  
  
  
  if((p >= -24 and p <= -5) and (p >= 5 and p <= 24) and (t > 0 and t > abs(p))){
    TDirection = 1;
    PDirection = 0;
  }
  if(( abs(p) == 25 ) and (t == 25 )){
    TDirection = 1;
    PDirection = 0;
  }
  if((p >= -3 and p <= 3) and (t >= 5)) {
    TDirection = 1;
    PDirection = 0;
  }
  
   
     if( (p >= -24 and p <= -5) and (p >= 5 and p <= 24) and ( t < 0 and t < (-1 * abs(p)))){
     TDirection = -1;
     PDirection = 0;
  }
  
  if( ( abs(p) == 25) and (t == -25 )){
     TDirection = -1;
     PDirection = 0;
  }
  
  if((p >= -3 and p <= 3) and t <= -5){
    TDirection = -1;
    PDirection = 0;
  }    

  if( (p < 5 and p > -5) and (t < 5 and t > -5) ){
//    noMove();
    TDirection = 0;
    PDirection = 0;
}

 if( outputValueY > 25 or outputValueY < -25){
   outputValueY = 0;
  }
 if( outputValueX > 25 or outputValueX < -25){
     outputValueX = 0;
  }
 if( outputValueZ > 25 or outputValueZ < -25){
    outputValueZ = 0;
  }
  if( outputValueT > 25 or outputValueT < -25){
    outputValueT = 0;
  }
 if( outputValueP > 25 or outputValueP < -25){
    outputValueP = 0;
  }
  
  SpeedY = YDirection * outputValueY;
  SpeedX = XDirection * outputValueX;
  SpeedZ = ZDirection * outputValueZ;
  SpeedT = TDirection * outputValueT; 
  SpeedP = PDirection * outputValueP;
  

  str1 = String(outputValueX);
  str2 = String(outputValueY);
  str3 = String(outputValueZ); 
  str4 = String(outputValueT); 
  str5 = String(outputValueP);

    
  strDirectY = String(YDirection);
  strDirectX = String(XDirection);
  strDirectZ = String(ZDirection);
  strDirectT = String(TDirection);
  strDirectP = String(PDirection);
  
 // if( SpeedY > 25 or SpeedY < -25){
   // SpeedY = 0;
  //}
 // if( SpeedX > 25 or SpeedX < -25){
   // SpeedX = 0;
  //}
  //if( SpeedZ > 25 or SpeedZ < -25){
   // SpeedZ = 0;
  //}
 // if( SpeedT > 25 or SpeedT < -25){
    //SpeedT = 0;
  //}
//  if( SpeedP > 25 or SpeedP < -25){
    //SpeedP = 0;
  //}
//Serial.println(strDirectT);  
  if(XDirection == 1){
    strDirectX = "L";
  }
  if(YDirection == 1){
    strDirectY = "F";
  }
  if(XDirection == -1){
    strDirectX = "R";
  }
  if(YDirection == -1){
    strDirectY = "B";
  }  
  if(ZDirection == 1){
    strDirectZ= "U";
  }
  if(ZDirection == -1){
    strDirectZ = "D";
  }
  if(TDirection == -1){
    strDirectT = "TD";    
  }
  if(TDirection == 1){
    strDirectT = "TU";
  }
  if(PDirection == -1){
  strDirectP = "RR";    
  }
  if(PDirection == 1){
    strDirectP = "RL";
  }


  SpeedY = abs(SpeedY);
  SpeedX = abs(SpeedX);
  SpeedZ = abs(SpeedZ);
  SpeedT = abs(SpeedT);
  SpeedP = abs(SpeedP);

  strSpeedY = String(SpeedY);
  strSpeedX = String(SpeedX);
  strSpeedZ = String(SpeedZ);
  strSpeedT = String(SpeedT);
  strSpeedP = String(SpeedP);


  if(strDirectY == "B"){
   strSpeedY = "-"+ String(SpeedY);
  }
  
  
   if(strDirectX == "L"){
   strSpeedX = "-"+ String(SpeedX); 
  }
   
  if(strDirectZ == "D"){
   strSpeedZ = "-"+ String(SpeedZ); 
  }
  if(strDirectT == "TD"){
   strSpeedT = "-"+ String(SpeedT);
  }
  
  if(strDirectP == "RL"){
   strSpeedP = "-"+ String(SpeedP); 
  }

rotMeasure = String(rotate);
ultimateStr = "R"+strSpeedX + "F"+ strSpeedY + "U"  +strSpeedZ + "T" +strSpeedT + "P"+ strSpeedP +"A"+ Button1 +"B"+ Button2+ "C"+ rotMeasure;
//Serial.println(ultimateStr);
//Serial.println(ultimateStr);
ultimateStr.toCharArray(joy,30);

Serial1.write(joy,30);


    Serial1.readBytes(m_str,45);
    
    String TempAndGyro = String(m_str);
    temp_in = TempAndGyro.substring(0,5);
    temp_out = TempAndGyro.substring(7,13);
    humidity = TempAndGyro.substring(15,20);
    leak = TempAndGyro.substring(22,23);
    gyroX = TempAndGyro.substring((TempAndGyro.indexOf("X") +1) , TempAndGyro.indexOf("Y"));
    gyroY = TempAndGyro.substring((TempAndGyro.indexOf("Y") +1) , TempAndGyro.length());
    
    Serial.println("Temp In: " +temp_in );
    Serial.println("Temp Out: " +temp_out );
    Serial.println("Humidity: " +humidity );
    Serial.println("Leak:" + leak);
    Serial.println("GyroX:" +gyroX);
    Serial.println("GyroY:"+ gyroY + ".\n");

    
}