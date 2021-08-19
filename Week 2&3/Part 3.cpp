// C++ code
//
const int LED=11;
int i = 0;

int buttonState = 0;

int LEDState = 0;

void setup()
{
  pinMode(2, INPUT);
  Serial.begin(9600);
  pinMode(11, OUTPUT);
}

void loop()
{
  Serial.println(digitalRead(2));
  Serial.println(LEDState);
  if (digitalRead(2) == 1) {
    buttonState = 1;
    LEDState = (LEDState + 1);
    LEDState = (LEDState % 6);
    while (digitalRead(2) == 1) {
    }
  } else {
    buttonState = 0;
  }
  if (buttonState == 1) {
    if (LEDState == 0) {
      analogWrite(LED,50);
    }
    if (LEDState == 1) {
      
      analogWrite(11, 100);
    }
    if (LEDState == 2) {
     
      analogWrite(11, 150);
    }
    if (LEDState == 3) {
     
      analogWrite(11, 200);
    }
    if (LEDState == 4) {
     
      analogWrite(11, 255);}

  }
  delay(10); // Delay a little bit to improve simulation performance
}
