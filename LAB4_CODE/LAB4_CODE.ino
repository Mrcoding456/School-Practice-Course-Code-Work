#include <Servo.h>
int servoPin = 9;
int switchPin = 2;
Servo servo1;
void setup() {
  // put your setup code here, to run once:
servo1.attach(servoPin);
pinMode(switchPin, INPUT_PULLUP);


}

void loop() {
  // put your main code here, to run repeatedly:
  setServoMotor(digitalRead(switchPin));
  
}
void setServoMotor(boolean reverse){
  if(reverse){
    servo1.write(180);
  }else{
    servo1.write(0);
  }
}
