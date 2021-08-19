// C++ code
//
int i = 0;

int buttonState = 0;

int LEDState = 0;

void setup()
{
  pinMode(2, INPUT);
  Serial.begin(9600);

  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop()
{
  Serial.println(digitalRead(2));
  Serial.println(LEDState);
  if (digitalRead(2) == 1) {
    buttonState = 1;
    LEDState = (LEDState + 1);
    LEDState = (LEDState % 4);
    while (digitalRead(2) == 1) {
    }
  } else {
    buttonState = 0;
  }
  if (buttonState == 1) {
    if (LEDState == 0) {
      digitalWrite(11, LOW);
      digitalWrite(12, LOW);
      digitalWrite(13, LOW);
    }
    if (LEDState == 1) {
      digitalWrite(11, LOW);
      digitalWrite(12, LOW);
      digitalWrite(13, HIGH);
    }
    if (LEDState == 2) {
      digitalWrite(11, LOW);
      digitalWrite(12, HIGH);
      digitalWrite(13, LOW);
    }
    if (LEDState == 3) {
      digitalWrite(11, HIGH);
      digitalWrite(12, LOW);
      digitalWrite(13, LOW);
    }
  }
  delay(10); // Delay a little bit to improve simulation performance
}
