char gyro_and_temp[25];

void setup() {
  // put your setup code here, to run once:
    Serial.begin(57600);
    //Serial1.begin(57600);
    delay(1000);
 
}

void loop() {
  /*
   * @author Alex
   * Recieving code in format: [X angle Reading , Y Angle Reading]
   */
    Serial.readBytes(gyro_and_temp,25);
    String Gyro_Temp = String(gyro_and_temp);
    Serial.println(Gyro_Temp);
    Serial.println(" ");
    delay(10);
    
}
