// C++ code
//
int sensorPin = 0;

void setup()
{
 pinMode(7,OUTPUT);
 pinMode(4,OUTPUT);
 pinMode(2,OUTPUT);
 Serial.begin(9600);
}

void loop()
{
  int volt = analogRead(sensorPin);
  double temp = volt * 5.0;
  temp /= 1024.0;
  temp = (temp - 0.5) * 100;
  Serial.print(temp);
  Serial.println(" C");
  
  if(temp >30)
  {
  digitalWrite(7,HIGH);
  digitalWrite(4,LOW);
  digitalWrite(2,LOW);
  delay(100);
  }
  if(30 >temp && temp > 12.5)
  {
  digitalWrite(7,LOW);
  digitalWrite(4,HIGH);
  digitalWrite(2,LOW);
  delay(100);
  }
  else
  {
  digitalWrite(7,LOW);
  digitalWrite(4,LOW);
  digitalWrite(2,HIGH);
  delay(100);
  }
  
  //delay(100);  Delay a little bit to improve simulation performance
}
