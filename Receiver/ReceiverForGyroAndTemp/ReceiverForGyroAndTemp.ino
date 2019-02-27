
char m_str[45];

void setup() {
  // put your setup code here, to run once:
    //Serial1.begin(57600);
        //Serial.begin(57600);
        Serial.begin(74880);

    delay(1000);
}

void loop() {
  /*
   * @author Alex000000000
   * Recieving code in format: [Temp inside, Temp outside, Humidity]
   */
    Serial.readBytes(m_str,45);
    
    String TempAndGyro = String(m_str);
    //String temp_in = TempAndGyro.substring(0,5);
    //String temp_out = TempAndGyro.substring(7,13);
    //String humidity = TempandGyro.substring(15,20);
    
    //Serial1.println("Temp In: " +temp_in );
    //Serial1.println("Temp Out: " +temp_out );
    //Serial1.println("Humidity: " +humidity );
   
    Serial.println(TempAndGyro); 
    Serial.println(" ");
    delay(300);
    
}
