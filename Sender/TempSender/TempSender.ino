
#define THERMISTORPIN A1         
// resistance at 25 degrees C
#define THERMISTORNOMINAL 10000      
// temp. for nominal resistance (almost always 25 C)
#define TEMPERATURENOMINAL 25   
// number of samples to take and average, more takes longer
#define NUMSAMPLES 5
// The beta coefficient of the thermistor (usually 3000-4000)
#define BCOEFFICIENT 3950
// the value of the 'other' resistor
#define SERIESRESISTOR 10000 
   
#include "DHT.h"
#define DHTPIN A0 // pin for connecting sensor
#define DHTTYPE DHT11 // DHT 11 : type of sensor you are using

DHT dht(DHTPIN, DHTTYPE);
String temp_in;
String humidity;
String Temp_Gyro; 
char m_Temp_Gyro[24];
char gyroData[25];
String GyroData;


String temp_out;
uint16_t samples[NUMSAMPLES];

 
void setup(void) {
  Serial.begin(57600);
  //Serial.println("DHT11 Moniter System");
  analogReference(EXTERNAL);  
  dht.begin();
  delay(10000);
}
 /////////////////////////////////
void loop(void) {
  
    /*
   * @author Alex
   * Sending code in format: [Temp inside, Temp outside, Humidity]
   * (Temp inside and Humidity : two decimal places  
   *  Temp outside : three decimaml places)
   */

  Serial.readBytes(gyroData,25);
  GyroData = String(gyroData);
  
  uint8_t i;
  float average;
 
  for (i=0; i< NUMSAMPLES; i++) {
   samples[i] = analogRead(THERMISTORPIN);
   delay(10);
  }
 
  average = 0;
  for (i=0; i< NUMSAMPLES; i++) {
     average += samples[i];
  }
  
  average /= NUMSAMPLES;
  average = 1023 / average - 1;
  average = SERIESRESISTOR / average;

 // Steinhart Equation;
  float steinhart;
  steinhart = average / THERMISTORNOMINAL;     
  steinhart = log(steinhart);                  
  steinhart /= BCOEFFICIENT;                
  steinhart += 1.0 / (TEMPERATURENOMINAL + 273.15); 
  steinhart = 1.0 / steinhart;                 
  steinhart -= 273.15;   // convert to C
  temp_out = String(steinhart,3);
  
// Read temperature as Celsius and humidity with Dht 11 Sensor
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  temp_in = String(t,2);
  humidity = String(h,2);


  Temp_Gyro = temp_in + " ,"+ temp_out + " ," + humidity + "X" + GyroData;
  Temp_Gyro.toCharArray(m_Temp_Gyro,40);
  Serial.write(m_Temp_Gyro,40);
 
  delay(300);
}
