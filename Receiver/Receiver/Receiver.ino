#include "Servo.h"
#include <Wire.h>


//Gyro Variables
float elapsedTime, time, timePrev;        //Variables for time control
int gyro_error=0;                         //We use this variable to only calculate once the gyro data error
float Gyr_rawX, Gyr_rawY, Gyr_rawZ;     //Here we store the raw data read 
float Gyro_angle_x, Gyro_angle_y;         //Here we store the angle value obtained with Gyro data
float Gyro_raw_error_x, Gyro_raw_error_y; //Here we store the initial gyro data error

//Acc Variables
int acc_error=0;                         //We use this variable to only calculate once the Acc data error
float rad_to_deg = 180/3.141592654;      //This value is for pasing from radians to degrees values
float Acc_rawX, Acc_rawY, Acc_rawZ;    //Here we store the raw data read 
float Acc_angle_x, Acc_angle_y;          //Here we store the angle value obtained with Acc data
float Acc_angle_error_x, Acc_angle_error_y; //Here we store the initial Acc data error

float Total_angle_x, Total_angle_y;
String Gyro, gyro_X, gyro_Y;
char gyro[20];

 
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

boolean twoMotors;
boolean fourMotors;



void setup() {
  Serial.begin(57600);
  Serial1.begin(57600);
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
  

  // put your setup code here, to run once:
 Wire.begin();                           //begin the wire comunication
  
  Wire.beginTransmission(0x68);           //begin, Send the slave adress (in this case 68)              
  Wire.write(0x6B);                       //make the reset (place a 0 into the 6B register)
  Wire.write(0x00);
  Wire.endTransmission(true);             //end the transmission
  //Gyro config
  Wire.beginTransmission(0x68);           //begin, Send the slave adress (in this case 68) 
  Wire.write(0x1B);                       //We want to write to the GYRO_CONFIG register (1B hex)
  Wire.write(0x10);                       //Set the register bits as 00010000 (1000dps full scale)
  Wire.endTransmission(true);             //End the transmission with the gyro
  //Acc config
  Wire.beginTransmission(0x68);           //Start communication with the address found during search.
  Wire.write(0x1C);                       //We want to write to the ACCEL_CONFIG register
  Wire.write(0x10);                       //Set the register bits as 00010000 (+/- 8g full scale range)
  Wire.endTransmission(true); 
  delay(1000);
    time = millis();
      if(acc_error==0)
  {
    for(int a=0; a<200; a++)
    {
      Wire.beginTransmission(0x68);
      Wire.write(0x3B);                       //Ask for the 0x3B register- correspond to AcX
      Wire.endTransmission(false);
      Wire.requestFrom(0x68,6,true); 
      
      Acc_rawX=(Wire.read()<<8|Wire.read())/4096.0 ; //each value needs two registres
      Acc_rawY=(Wire.read()<<8|Wire.read())/4096.0 ;
      Acc_rawZ=(Wire.read()<<8|Wire.read())/4096.0 ;

      
      /*---X---*/
      Acc_angle_error_x = Acc_angle_error_x + ((atan((Acc_rawY)/sqrt(pow((Acc_rawX),2) + pow((Acc_rawZ),2)))*rad_to_deg));
      /*---Y---*/
      Acc_angle_error_y = Acc_angle_error_y + ((atan(-1*(Acc_rawX)/sqrt(pow((Acc_rawY),2) + pow((Acc_rawZ),2)))*rad_to_deg)); 
      
      if(a==199)
      {
        Acc_angle_error_x = Acc_angle_error_x/200;
        Acc_angle_error_y = Acc_angle_error_y/200;
        acc_error=1;
      }
    }
  }//end of acc error calculation   


/*Here we calculate the gyro data error before we start the loop
 * I make the mean of 200 values, that should be enough*/
  if(gyro_error==0)
  {
    for(int i=0; i<200; i++)
    {
      Wire.beginTransmission(0x68);            //begin, Send the slave adress (in this case 68) 
      Wire.write(0x43);                        //First adress of the Gyro data
      Wire.endTransmission(false);
      Wire.requestFrom(0x68,4,true);           //We ask for just 4 registers 
         
      Gyr_rawX=Wire.read()<<8|Wire.read();     //Once again we shif and sum
      Gyr_rawY=Wire.read()<<8|Wire.read();
   
      /*---X---*/
      Gyro_raw_error_x = Gyro_raw_error_x + (Gyr_rawX/32.8); 
      /*---Y---*/
      Gyro_raw_error_y = Gyro_raw_error_y + (Gyr_rawY/32.8);
      if(i==199)
      {
        Gyro_raw_error_x = Gyro_raw_error_x/200;
        Gyro_raw_error_y = Gyro_raw_error_y/200;
        gyro_error=1;
      }
    }
  }//end of gyro error calculation   
}

void loop() {
   timePrev = time;                        // the previous time is stored before the actual time read
  time = millis();                        // actual time read
  elapsedTime = (time - timePrev) / 1000; //divide by 1000 in order to obtain seconds

  //////////////////////////////////////Gyro read/////////////////////////////////////

    Wire.beginTransmission(0x68);            //begin, Send the slave adress (in this case 68) 
    Wire.write(0x43);                        //First adress of the Gyro data
    Wire.endTransmission(false);
    Wire.requestFrom(0x68,4,true);           //We ask for just 4 registers
        
    Gyr_rawX=Wire.read()<<8|Wire.read();     //Once again we shif and sum
    Gyr_rawY=Wire.read()<<8|Wire.read();
    /*Now in order to obtain the gyro data in degrees/seconds we have to divide first
    the raw value by 32.8 because that's the value that the datasheet gives us for a 1000dps range*/
    /*---X---*/
    Gyr_rawX = (Gyr_rawX/32.8) - Gyro_raw_error_x; 
    /*---Y---*/
    Gyr_rawY = (Gyr_rawY/32.8) - Gyro_raw_error_y;
    
    /*Now we integrate the raw value in degrees per seconds in order to obtain the angle
    * If you multiply degrees/seconds by seconds you obtain degrees */
    /*---X---*/
    Gyro_angle_x = Gyr_rawX*elapsedTime;
    /*---X---*/
    Gyro_angle_y = Gyr_rawY*elapsedTime;


    
  
  //////////////////////////////////////Acc read/////////////////////////////////////

  Wire.beginTransmission(0x68);     //begin, Send the slave adress (in this case 68) 
  Wire.write(0x3B);                 //Ask for the 0x3B register- correspond to AcX
  Wire.endTransmission(false);      //keep the transmission and next
  Wire.requestFrom(0x68,6,true);    //We ask for next 6 registers starting withj the 3B  
  /*We have asked for the 0x3B register. The IMU will send a brust of register.
  * The amount of register to read is specify in the requestFrom function.
  * In this case we request 6 registers. Each value of acceleration is made out of
  * two 8bits registers, low values and high values. For that we request the 6 of them  
  * and just make then sum of each pair. For that we shift to the left the high values 
  * register (<<) and make an or (|) operation to add the low values.
  If we read the datasheet, for a range of+-8g, we have to divide the raw values by 4096*/    
  Acc_rawX=(Wire.read()<<8|Wire.read())/4096.0 ; //each value needs two registres
  Acc_rawY=(Wire.read()<<8|Wire.read())/4096.0 ;
  Acc_rawZ=(Wire.read()<<8|Wire.read())/4096.0 ; 
 /*Now in order to obtain the Acc angles we use euler formula with acceleration values
 after that we substract the error value found before*/  
 /*---X---*/
 Acc_angle_x = (atan((Acc_rawY)/sqrt(pow((Acc_rawX),2) + pow((Acc_rawZ),2)))*rad_to_deg) - Acc_angle_error_x;
 /*---Y---*/
 Acc_angle_y = (atan(-1*(Acc_rawX)/sqrt(pow((Acc_rawY),2) + pow((Acc_rawZ),2)))*rad_to_deg) - Acc_angle_error_y;    


 //////////////////////////////////////Total angle and filter////U/////////////////////////////////
 /*---X axis angle---*/
 Total_angle_x = 0.98 *(Total_angle_x + Gyro_angle_x) + 0.02*Acc_angle_x;
 /*---Y axis angle---*/
 Total_angle_y = 0.98 *(Total_angle_y + Gyro_angle_y) + 0.02*Acc_angle_y;


  Joystick = String(joy);
  //Serial.println(Joystick);
 // Serial.println(Joystick);
  //digitalWrite(LED_BUILTIN, HIGH);
  
  SideSpeed = Joystick.substring((Joystick.indexOf("R") + 1), Joystick.indexOf("F"));
  FBSpeed = Joystick.substring((Joystick.indexOf("F") + 1), Joystick.indexOf("U"));
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
    
          speed07 = map(fbSpeed, 0, 25, 1500, 1275);
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
          speed09 = map(fbSpeed, 0, 25, 1500, 1715);
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
    
        speed01 = map(sideSpeed, 0, 25, 1500, 1715);
        speed02 = map(sideSpeed, 0, 25, 1500, 1275);
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
    
    speed01 = map(sideSpeed, 0, 25, 1500, 1715);
    speed02 = map(sideSpeed, 0, 25, 1500, 1275);
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
    
        speed03 = map(turnSpeed, 0, 25, 1500, 1715);
        speed04 = map(turnSpeed, 0, 25, 1500, 1275);
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
    
        speed03 = map(turnSpeed, 0, 25, 1500, 1715);
        speed04 = map(turnSpeed, 0, 25, 1500, 1275);
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

 gyro_X = String(Total_angle_x,2);
 gyro_Y = String(Total_angle_y,2);
 Gyro = "45 :"+ gyro_X + ", " + gyro_Y;
 Gyro.toCharArray(gyro,20);
 Wire.write(gyro,20);
 Serial1.write(gyro,20); 
  Serial1.readBytes(joy,25);



  
    
  }