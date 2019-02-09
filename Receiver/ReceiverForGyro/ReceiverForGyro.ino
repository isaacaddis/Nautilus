char m_gyro[25];

void setup() {
  // put your setup code here, to run once:
    Serial.begin(57600);
    Serial1.begin(57600);
 
}

void loop() {
  /*
   * @author Alex
   * Recieving code in format: [Temp inside, Temp outside, Humidity]
   */
    Serial1.readBytes(m_gyro,25);
    String Gyro = String(m_gyro);
    Serial.println(Gyro);
    Serial.println(" ");
    delay(300);
    
}
