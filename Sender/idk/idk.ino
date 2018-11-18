                        

#include "Servo.h"

const int InputA0 = A0;
int PotA0 = 0;        // value read from the pot
int SpeedA0 = 0;
const int InputA1 = A1;
int PotA1 = 0;        // value read from the pot
int SpeedA1 = 0;
int outputValueX = 0;
int outputValueY = 0;
int n = 0;
String str1;
String str2;
String str3;
String str4;
String str5;


Servo f_Left;
Servo f_Right;
Servo b_Left;
Servo b_Right;

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

  Serial.println("Current Command: Move Forward");
  Serial.println(" ");
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

  Serial.println("Current Command: Move Backward");
  Serial.println(" ");
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

  
  Serial.println("Current Command: Move Left");
  Serial.println(" ");
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

  Serial.println("Current Command: Move Right");
  Serial.println(" ");
}

void setup() {
  // Begin the Serial at 9600 Baud
f_Left.attach(8);
f_Right.attach(9);
b_Left.attach(10);
b_Right.attach(11);
 delay(500);
  Serial.begin(9600);
}

void loop() {
  PotA0 = analogRead(InputA0);
  PotA1 = analogRead(InputA1);
  outputValueX = map(PotA0, 0, 1023, -10, 10);
  outputValueY = map(PotA1, 0, 1023, -10, 10);




   



    
//  if(outputValueY < 0 and (outputValueX >= -3 and outputValueX <= 3)){ 
//  goBackward(outputValueY); 
//   }
//  else if(outputValueY > 0 and (outputValueX >= 7 and outputValueX <= - 7)){ 
//    goForward(outputValueY); 
//   }
// if(outputValueX < 0 and (outputValueY >= -6 and outputValueY <= 6)){ 
//   goRight(outputValueX); 
//   }
// else if(outputValueX > 0 and (outputValueY >= -3 and outputValueY <= 3)){ 
//   goLeft(outputValueX); 
//  }

//  if(outputValueY < 0 and (outputValueX >= -2 and outputValueX <= 2)){ 
//    goBackward(outputValueY); 
//   }
//  else if(outputValueY > 0 and (outputValueX >= -2 and outputValueX <= 2)){ 
//    goForward(outputValueY); 
//   }
//  if(outputValueX < 0 and (outputValueY >= -2 and outputValueY <= 2)){ 
//    goRight(outputValueX); 
//   }
//  else if(outputValueX > 0 and (outputValueY >= -2 and outputValueY <= 2)){ 
//    goLeft(outputValueX); 
//   }

  
  str1=String(outputValueX);
  str2=String(outputValueY); 
  str3=String(str1+ " , " + str2);
  //str4=String(SpeedA0);
  //str5=String(SpeedA1);

  
  
  Serial.println("X Position: ");
  Serial.println(str1); //Write the serial data
  Serial.println("Y Position: ");
  Serial.println(str2); //Write the serial data
  // Serial.println(" ");
  Serial.println("X and Y Coordinates: ");
  Serial.println(str3);
  
  delay(100);
//   Serial.println("SpeedAO : "); //Write the serial data
//   Serial.println(str4);
 //  Serial.println("SpeedA1 : "); //Write the serial data
 //  Serial.println(str5);

  

 delay(100);
}
