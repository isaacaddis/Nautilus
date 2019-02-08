
char m_str[24];

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
}

void loop() {
  /*
   * @author Alex
   * Recieving code in format: [Temp inside, Temp outside, Humidity]
   */
    Serial.readBytes(m_str,24);
    String Temp = String(m_str);
    String temp_in = Temp.substring(0,5);
    String temp_out = Temp.substring(7,13);
    String humidity = Temp.substring(15,20);
    
    Serial.println("Temp In: " +temp_in );
    Serial.println("Temp Out: " +temp_out );
    Serial.println("Humidity: " +humidity );
    Serial.println(" ");
    delay(1000);
    
}
