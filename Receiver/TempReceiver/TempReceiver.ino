
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
    Serial.println(Temp);
    Serial.println(" ");
    delay(1000);
    
}
