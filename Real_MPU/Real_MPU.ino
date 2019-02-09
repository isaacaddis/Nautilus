#include<Wire.h>

const int MPU6050_addr=0x68;
int16_t AccX,AccY,AccZ,Temp,GyroX,GyroY,GyroZ;
float Acceleration_angle_X , Acceleration_angle_Y;
float Total_angle_X, Total_angle_Y;
float rad_to_deg = 180/3.141592654;
float elapsedTime, time, timePrev;
String angle_x;
String angle_y;
String gyro_z;
String Gyro;
char gyro[19];


void setup(){
  Wire.begin();
  Wire.beginTransmission(MPU6050_addr);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(57600);
  Serial2.begin(57600);
  time = millis(); //Start counting time in milliseconds


}
void loop(){
  timePrev = time;  // the previous time is stored before the actual time read
  time = millis();  // actual time read
  elapsedTime = (time - timePrev) / 1000; 
  Wire.beginTransmission(MPU6050_addr);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU6050_addr,6,true);
  AccX=Wire.read()<<8|Wire.read();
  AccY=Wire.read()<<8|Wire.read();
  AccZ=Wire.read()<<8|Wire.read();
  Temp=Wire.read()<<8|Wire.read();
   /*---X---*/
  Acceleration_angle_X = atan((AccY/16384.0)/sqrt(pow((AccX/16384.0),2) + pow((AccZ/16384.0),2)))*rad_to_deg;
     /*---Y---*/
  Acceleration_angle_Y = atan(-1*(AccX/16384.0)/sqrt(pow((AccY/16384.0),2) + pow((AccZ/16384.0),2)))*rad_to_deg;
 
  Wire.beginTransmission(0x68);
  Wire.write(0x43); //Gyro data first adress
  Wire.endTransmission(false);
  Wire.requestFrom(0x68,4,true);
  GyroX=Wire.read()<<8|Wire.read();
  GyroY=Wire.read()<<8|Wire.read();
  GyroZ=Wire.read()<<8|Wire.read();
  GyroX = GyroX / 131.0;
  GyroY = GyroY / 131.0;
  GyroZ = GyroZ / 131.0;
  /*---X axis angle---*/
  Total_angle_X = 0.98 *(Total_angle_X + GyroX*elapsedTime) + 0.02*Acceleration_angle_X;
  /*---Y axis angle---*/
  Total_angle_Y = 0.98 *(Total_angle_Y + GyroY*elapsedTime) + 0.02*Acceleration_angle_Y;
  angle_x = String(GyroX);
  angle_y = String(GyroY);
  //gyro_z = String(GyroZ);
  Gyro = angle_x + ", " + angle_y ;
  Gyro.toCharArray(gyro, 19);
  Wire.write(gyro,19);
  Serial2.write(gyro,19);
  //Serial.println(" ");
  
//  Serial.print("AccX = "); Serial.print(AccX);
//  Serial.print(" || AccY = "); Serial.print(AccY);
//  Serial.print(" || AccZ = "); Serial.print(AccZ);
//  Serial.print(" || Temp = "); Serial.print(Temp/340.00+36.53);
//  Serial.print(" || GyroX = "); Serial.print(GyroX);
//  Serial.print(" || GyroY = "); Serial.print(GyroY);
//  Serial.print(" || GyroZ = "); Serial.println(GyroZ); 

  delay(300);
}
