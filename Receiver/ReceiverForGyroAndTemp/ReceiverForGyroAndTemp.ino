
char m_str[40];

void setup() {
  // put your setup code here, to run once:
    Serial1.begin(9600);
}

void loop() {
  /*
   * @author Alex
   * Recieving code in format: [Temp inside, Temp outside, Humidity]
   */
    Serial1.readBytes(m_str,40);
    String TempAndGyro = String(m_str);
    //String temp_in = TempAndGyro.substring(0,5);
    //String temp_out = TempAndGyro.substring(7,13);
    //String humidity = TempandGyro.substring(15,20);
    
    //Serial1.println("Temp In: " +temp_in );
    //Serial1.println("Temp Out: " +temp_out );
    //Serial1.println("Humidity: " +humidity );
   
    Serial1.println(TempAndGyro); 
    Serial1.println(" ");
    delay(500);
    
}
