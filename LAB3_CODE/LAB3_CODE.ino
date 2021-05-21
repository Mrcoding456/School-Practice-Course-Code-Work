





int enablePin = 3;
int in1Pin = 4;
int in2Pin = 5;
int switchPin = 2;

void setMotor(boolean reverse) {
analogWrite(enablePin, 200); // 0~255
digitalWrite(in1Pin, !reverse);
digitalWrite(in2Pin, reverse);

}


void setup() {
pinMode(in1Pin, OUTPUT);
pinMode(in2Pin, OUTPUT);
pinMode(enablePin, OUTPUT);
pinMode(switchPin, INPUT_PULLUP);


}




void loop() {
  // put your main code here, to run repeatedly:

  boolean reverse = digitalRead(switchPin); // Receive input
  setMotor(reverse); //OOP Code


}
