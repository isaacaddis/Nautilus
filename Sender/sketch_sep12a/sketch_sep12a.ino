int InputA0 = A0;
int InputA1 = A1;
int PotA0;
int PotA1;
int SpeedA0 = 0;
int SpeedA1 = 0;
void setup() {
  // put your setup code here, to run once:
  int PotA0 = analogRead(InputA0);
  int PotA1 = analogRead(InputA1);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  int PotA0 = analogRead(InputA0);
  int PotA1 = analogRead(InputA1);
  
  SpeedA0 = map(PotA0, 0, 1023, -10, 10);
  SpeedA1 = map(PotA1, 0, 1023, -10, 10);

  Serial.println(SpeedA0);
  Serial.println(SpeedA1);
  delay(100);
  
}
