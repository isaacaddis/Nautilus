#include "Servo.h"
#define max_len 37

//

const int InputA0 = A0; // Forward and Backward
const int InputA1 = A1; // Left and Right
const int InputA2 = A2; // Up and down
const int InputA3 = A3; // Tilt 
const int InputA4 = A4; // Turning



int PotA0 = 0;        // value read from the pot
int SpeedA0 = 0;
int PotA1 = 0;// value read from the pot
int SpeedA1 = 0;
int PotA2 = 0;
int SpeedA2 = 0;
int PotA3 = 0;
int SpeedA3= 0;
int PotA4 = 0;
int SpeedA4= 0;



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

char sendsig[max_len];

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

String strDirectX;
String strDirectY;
String strDirectZ; 
String strDirectT;
String strDirectP; 

String ultimateStr;


const int unitOne = 1;

boolean Left;
boolean Right;
boolean Forward;
boolean Backward;
boolean Up;
boolean Down;
boolean bTilt;
boolean fTilt;
boolean CounterCW;
boolean Clockwise;

boolean Pan;
boolean Vertical;
boolean Tilt;
boolean Pivot;


Servo f_Left;
Servo f_Right;
Servo b_Left;
Servo b_Right;
Servo vert_Motor1;
Servo vert_Motor2;

void goForward(int param) {
  int percent = abs(param / 10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  f_Left.write(velocity * -1);
  f_Right.write(velocity * -1);
  b_Left.write(velocity * -1);
  b_Right.write(velocity * -1);

//  Serial.println("Current Command: Move Forward");

}

void goBackward(int param) {
  int percent = abs(param / 10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  f_Left.write(velocity);
  f_Right.write(velocity);
  b_Left.write(velocity);
  b_Right.write(velocity);

//  Serial.println("Current Command: Move Backward");
  
}

void goLeft(int param) {
  int percent = abs(param/10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  f_Left.write(velocity);
  f_Right.write(velocity * -1);
  b_Left.write(velocity * -1);
  b_Right.write(velocity);

// Serial.println("Current Command: Move Left");

}
void goRight(int param) {
  int percent = abs(param/10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  f_Left.write(velocity * -1);
  f_Right.write(velocity);
  b_Left.write(velocity);
  b_Right.write(velocity * -1);

//  Serial.println("Current Command: Move Right");

}

void noMove() {
  int velocity = 0;
  f_Left.write(velocity);
  f_Right.write(velocity);
  b_Left.write(velocity);
  b_Right.write(velocity );

//  Serial.println("Current Command: Don't Move");
}

void goVertical(int param, boolean direct){
  int percent = abs(param/10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  if(direct){
    vert_Motor1.write(velocity);
    vert_Motor2.write(velocity);
  }
  else{
    vert_Motor1.write(velocity * -1);
    vert_Motor2.write(velocity * -1);
  }
}

void goTilt(int param, boolean direct) {
  int percent = abs(param/10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  if(direct){
    vert_Motor1.write(velocity *-1);
    vert_Motor2.write(velocity);
  }
  else{
    vert_Motor1.write(velocity);
    vert_Motor2.write(velocity * -1);
  }

 void goPivot( int param, boolean Clockwise){
  int percent = abs(param/10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  if (Clockwise) {
    f_Left.write( velocity * -1);
    b_Left.write( velocity * -1);
    f_Right.write(velocity * 1);
    b_Right.write(velocity * 1);
  }
  else if (CounterCW) {
    f_Left.write(velocity *1);
    b_Left.write(velocity *1);
    f_Right.write(velocity * -1);
    f_Right.write(velocity * -1);
    
  }
 }
}

void setup() {
  // Begin the Serial at 9600 Baud
f_Left.attach(8);
f_Right.attach(9);
b_Left.attach(10);
b_Right.attach(11);
vert_Motor1.attach(12);
vert_Motor2.attach(13);
 delay(500);
  Serial.begin(9600);
}

void loop() {
  PotA0 = analogRead(InputA0);
  PotA1 = analogRead(InputA1);
  PotA2 = analogRead(InputA2);
  PotA3 = analogRead(InputA3);
  PotA4 = analogRead(InputA4);
  
  
  outputValueY = map(PotA0, 0, 1023, -10, 10);
  outputValueX = map(PotA1, 0, 1023, -10, 10);
  outputValueZ = map(PotA2, 0, 1023, -10, 10);
  outputValueT = map(PotA3, 0, 1023, -10, 10);
  outputValueP = map(PotA4, 0, 1023, -10, 10);
  
  int x = outputValueX;
  int y = outputValueY; 
  int z = outputValueZ;
  int t = outputValueT;
  int p = outputValueP;

  if( ((x <= -2 and x >= -9) and abs(x) != unitOne) and ((abs(y) >= x ) and y != 10)){
    goLeft(outputValueX);
    XDirection = -1;
    YDirection = 0;
    boolean Left = true;
    boolean Right = false;
    boolean Forward = false;
    boolean Backward = false;
}
  else if((x == -10) and (abs(y) <= 9)){
    goLeft(outputValueX);
    XDirection = -1;
    YDirection = 0;
    boolean Left = true;
    boolean Right = false;
    boolean Forward = false;
    boolean Backward = false;
}
       
  if( (x >= 2 and x <= 9) and (abs(y) <= x)){
    goRight(outputValueX);
    XDirection = 1;
    YDirection = 0;
    boolean Left = false;
    boolean Right = true;
    boolean Forward = false;
    boolean Backward = false;
  }
  else if((x == 10) and ( abs(y) <= 9)){
    goRight(outputValueX);
    XDirection = 1;
    YDirection = 0;
    boolean Left = false;
    boolean Right = true;
    boolean Forward = false;
    boolean Backward = false;
  }

 
  if( ((x >= -9 and x <= 9) and y != 1) and (y > abs(x))){
    goForward(outputValueY);
    YDirection = 1;
    XDirection = 0;
    boolean Left = false;
    boolean Right = false;
    boolean Forward = true;
    boolean Backward = false;
  }
  if( ( abs(x) == 10 ) and (y == 10 )){
    goForward(outputValueY);
    YDirection = 1;
    XDirection = 0;
    boolean Left = false;
    boolean Right = false;
    boolean Forward = true;
    boolean Backward = false;
  }
  else if((x == 0) and (y >= 2 and abs(y) != unitOne) ){
    goForward(outputValueY);
    YDirection = 1;
    XDirection = 0;
    boolean Left = false;
    boolean Right = false;
    boolean Forward = true;
    boolean Backward = false;
  }
  
   
  if( ((x >= -9 and x <= 9 ) and x != 1) and (abs(y) < abs(x) * -1 )){
     goBackward(outputValueY);
     YDirection = -1;
     XDirection = 0;
    boolean Left = false;
    boolean Right = false;
    boolean Forward = false;
    boolean Backward = true;
  }
  if( ( abs(x) == 10 ) and (y == -10 )){
     goBackward(outputValueY);
     YDirection = -1;
     XDirection = 0;
    boolean Left = false;
    boolean Right = false;
    boolean Forward = false;
    boolean Backward = true;
  }
  else if((x == 0) and (y <= -2 and abs(y) != unitOne) ){
    goBackward(outputValueY);
    YDirection = -1;
    XDirection = 0;
    boolean Left = false;
    boolean Right = false;
    boolean Forward = false;
    boolean Backward = true;
  }    

  if( (x < 2 and x > -2) and (y < 2 and y > -2) ){
//    noMove();
    YDirection = 0;
    XDirection = 0;
    boolean Left = false;
    boolean Right = false;
    boolean Forward = false;
    boolean Backward = false; 

}
 // if(!(Left) and !(Right) and !(Forward) and !(Backward)){
   
  if(z >= 2){
     goVertical(outputValueZ, true);
     ZDirection = 1;
//     x = 0;
//     y = 0;
//     YDirection = 0;
//     XDirection = 0; 
     boolean Up = true;
     boolean Down = false;
   }
    if(z <= -2){
     goVertical(outputValueZ, false);
     ZDirection = -1;
//     x = 0;
//     y = 0;
//     YDirection = 0;
//     XDirection = 0;
     boolean Up = false;
     boolean Down = true;
   }
    else if ((z< 2) and (z> -2 )) {
//     noMove();
//     YDirection = 0;
//     XDirection = 0;
       ZDirection = 0;
       boolean Up = false;
       boolean Down = false;
   }
  

  if( ((p <= -2 and p >= -9) and abs(p) != unitOne) and ((abs(t) >= p ) and t != 10)){
    goPivot(outputValueP, false);
    PDirection = -1;
    TDirection = 0;
    boolean CounterCW = true;
    boolean Clockwise= false;
    boolean fTilt= false;
    boolean bTilt= false;
}
  else if((p == -10) and (abs(t) <= 9)){
    goPivot(outputValueP, false);
    PDirection = -1;
    TDirection = 0;
    boolean CounterCW= true;
    boolean Clockwise = false;
    boolean fTilt = false;
    boolean bTilt = false;
}
       
  if( (p >= 2 and p <= 9) and (abs(t) <= p)){
    goPivot(outputValueP, true);
    PDirection = 1;
    TDirection = 0;
    boolean CounterCW = false;
    boolean Clockwise = true;
    boolean fTilt = false;
    boolean bTilt = false;
  }
  else if((p == 10) and ( abs(t) <= 9)){
    goPivot(outputValueP, true);
    PDirection = 1;
    TDirection = 0;
    boolean CounterCW = false;
    boolean Clockwise = true;
    boolean fTilt = false;
    boolean bTilt = false;
  }

 
  if( ((p >= -9 and p <= 9) and t != 1) and (t > abs(p))){
    goTilt(outputValueT, true);
    TDirection = 1;
    PDirection = 0;
    boolean CounterCW = false;
    boolean Clockwise = false;
    boolean fTilt = true;
    boolean bTilt = false;
  }
  if( ( abs(p) == 10 ) and (t == 10 )){
    goTilt(outputValueT, true);
    TDirection = 1;
    PDirection = 0;
    boolean CounterCW = false;
    boolean Clockwise = false;
    boolean fTilt = true;
    boolean bTilt = false;
  }
  else if((p == 0) and (t >= 2 and abs(t) != unitOne) ){
    goTilt(outputValueT, true);
    TDirection = 1;
    PDirection = 0;
    boolean CounterCW = false;
    boolean Clockwise = false;
    boolean fTilt = true;
    boolean bTilt = false;
  }
  
   
  if( ((p >= -9 and p <= 9 ) and p != 1) and (abs(t) < abs(p) * -1 )){
     goTilt(outputValueT, false);
     TDirection = -1;
     PDirection = 0;
    boolean CounterCW = false;
    boolean Clockwise = false;
    boolean fTilt = false;
    boolean bTilt = true;
  }
  if( ( abs(p) == 10 ) and (t == -10 )){
     goTilt(outputValueT, false);
     TDirection = -1;
     PDirection = 0;
    boolean CounterCW = false;
    boolean Clockwise = false;
    boolean fTilt = false;
    boolean bTilt = true;
  }
  else if((p == 0) and (t <= -2 and abs(t) != unitOne) ){
    goTilt(outputValueT, false);
    TDirection = -1;
    PDirection = 0;
    boolean CounterCW = false;
    boolean Clockwise = false;
    boolean fTilt = false;
    boolean bTilt = true;
  }    

  if( (p < 2 and p > -2) and (t < 2 and t > -2) ){
//    noMove();
    TDirection = 0;
    PDirection = 0;
    boolean CounterCW = false;
    boolean Clockwise = false;
    boolean fTilt = false;
    boolean bTilt = false; 

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
  
  if(XDirection == 1){
    strDirectX = "R";
  }
  if(YDirection == 1){
    strDirectY = "F";
  }
  if(XDirection == -1){
    strDirectX = L";
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
    strDirectT = "-1";    
  }
  if(TDirection == 1){
    strDirectT = "+1";
  }
  
  strSpeedY = String(SpeedY);
  strSpeedX = String(SpeedX);
  strSpeedZ = String(SpeedZ);
  strSpeedT = String(SpeedT);
  strSpeedP = String(SpeedP);

 if((Left) or (Right) or (Forward) or (Backward)){
    boolean Pan = true;    
 }

 if((CounterCW) or (Clockwise)){
    boolean Pivot = true;    
 }
  
 if((fTilt) or (bTilt)){
    boolean Tilt = true;    
 }
 
 if((Up) or (Down)){
    boolean Vertical = true;    
 }


 if ((Pan) and (Pivot) and (Tilt) and (Vertical)){
    // string length  = ranges from 32-37
     
    ultimateStr = String(strDirectX + " ," + strSpeedX + " ," + strDirectY  + " ," + strSpeedY + " ,"  + strDirectZ + " ," + strSpeedZ + " ," + strDirectT + " ," + strSpeedT + ' ,"+ strDirectP + " ," + strSpeedP +"\n");
 }

 
 if( !(Pan)){
    if((Vertical) and (Tilt) and (Pivot)){ 
      // string length = 
      ultimateStr = String(strDirectZ + " ," + strSpeedZ + " ,"+ strDirectT + " ," + strSpeedT + " ,"+ strDirectP + " ," + strSpeedP +"\n");
    }
    if( !(Vertical) and (Tilt)and (Pivot) )){
      ultimateStr = String(strDirectT + " ," + strSpeedT + " ,"+ strDirectP + " ," + strSpeedP +"\n");
    }
    if( !(Vertical) and !(Tilt) and (Pivot)){
      ultimateStr = String(strDirectP + " ," + strSpeedP +"\n");
    }
    if( (Vertical) and (Tilt) and !(Pivot)){
      ultimateStr = String(strDirectZ + " ," + strSpeedZ + " ,"+ strDirectT + " ," + strSpeedT + "\n");
    }
    if( (Vertical) !(Tilt) and (Pivot)){
      ultimateStr = String(strDirectZ + " ," + strSpeedZ + " ,"+ strDirectP + " ," + strSpeedP +"\n");
    }
    if( !(Vertcial) and (Tilt) and !(Pivot){
      ultimateStr = String(strDirectT + " ," + strSpeedT +"\n");
    }
    if((Vertical) and !(Tilt) and !(Pivot){
      ultimateStr = String(strDirectZ + " ," + strSpeedZ + "\n");  
    }
  }
  else if ((Pan)) {
    if( !(Vertical) and ! (Tilt) and !(Pivot)){
      ultimateStr = String(strDirectX + " ," + strSpeedX  + " ,"  + strDirectY + " ," + strSpeedY +"\n");
    }
    if( (Vertical) and !(Tilt) and !(Pivot)){
      ultimateStr = String(strDirectX + " ," + strSpeedX  + " ," +strDirectY + " ," + strSpeedY + " ,"  + strDirectZ + " ," + strSpeedZ +"\n");
    }
    if( (Vertical) and (Tilt) and ! (Pivot)) {
      ultimateStr = String(strDirectX + " ," + strSpeedX  + " ," + strDirectY + " ," + strSpeedY + " ,"  + strDirectZ + " ," + strSpeedZ + " ," + strDirectT + " ," + strSpeedT +"\n");
    }
    if( !(Vertical) and !(Tilt) and (Pivot)){
      ultimateStr = String(strDirectX + " ," +  strSpeedX  + " ," + strDirectY + " ," + strSpeedY + " ," +strDirectP + " ," + strSpeedP +"\n");
    }
    if( !(Vertical) and (Tilt) and !(Pivot){
      ultimateStr = String(strDirectX + " ," + strSpeedX + " ," +  strDirectY + " ," + strSpeedY + " ," + strDirectT + " ," + strSpeedT + "\n");  
    }
    if( !(Vertical) and (Tilt) and (Pivot)){
      ultimateStr = String(strDirectX + " ," + strSpeedX+ " ," + strDirectY  + " ," + strSpeedY + " ,"  + strDirectT + " ," + strSpeedT + " , "+ strDirectP + " ," + strSpeedP +"\n");
    }
    if( (Vertical) and !(Tilt) and (Pivot)){
      ultimateStr = String(strDirectX + " ," + strSpeedX + " ," +  strDirectY + " ," + strSpeedY + " ,"  + strDirectZ + " ," + strSpeedZ + ' , "+ strDirectP + " ," + strSpeedP +"\n");
    }
  }

  
//  Serial.println("X and Y Coordinates: ");
//  Serial.println(str3);
//  
//  Serial.println("Speed along the Y axis: ");
//  Serial.println(strSpeedY);
//    
//  Serial.println("Speed along the X axis: ");
//  Serial.println(strSpeedX);
//
//  Serial.println("Direction along the Y axis: ");
//  Serial.println(strDirectY);
//  
//  Serial.println("Direction along the X axis: ");
//  Serial.println(strDirectX);
//  
 
//  strDirectY.toCharArray(sendsig, 3);
//  strDirectX.toCharArray(sendsig, 3);
//  strSpeedX.toCharArray(sendsig, 3);
//  strSpeedY.toCharArray(sendsig, 3);

ultimateStr.toCharArray(sendsig,max_len );
Serial.write(sendsig,max_len ); //Write the serial data 
 

  delay(100);

}
  
