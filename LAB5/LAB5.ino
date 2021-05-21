
#include <Servo.h> //library
int servoPin = 9; //pwm to control angle
Servo servo1;

int trigPin = 13;
int echoPin = 11;
long duration;
long distance;




void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin, INPUT);

  servo1.attach(servoPin);




}

long microsecondsToCentimeter(long time){
  return time*0.034/2;
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = microsecondsToCentimeter(duration);
  Serial.print("The distance to the target is: ");
  Serial.print(distance);
  Serial.print(" centimeters.");
  delay(1000);
  
  int position;
  servo1.write(0); //90 degree
  delay(1000); // spare time for moving servo 
  servo1.write(180); //180 
  delay(1000); 
  servo1.write(0); //0 
  delay(1000);
  for(position = 0; position < 180; position += 2) {
    servo1.write(position);
    delay(3);
    }
    for(position = 180; position >= 0; position -= 2) {
      servo1.write(position);
      delay(3);
      }  }
