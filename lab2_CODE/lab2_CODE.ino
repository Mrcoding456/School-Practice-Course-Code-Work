
class Flasher{

int ledPin;
long OnTime;
long OffTime;
int ledState;
unsigned long previousMillis;
long intervalTime;

public:
Flasher(int pin, long on, long off, long interval){
  ledPin = pin;
  pinMode(ledPin, OUTPUT);
  OnTime =on;
  OffTime = off;
  ledState = LOW;
  previousMillis = 0;
  intervalTime=interval;

}

void Update(){
    unsigned long currentMillis = millis()+intervalTime;
    if((ledState==HIGH) && (currentMillis-previousMillis >= OnTime)){
      ledState =LOW;
      previousMillis =currentMillis;
      digitalWrite(ledPin,ledState);
    }else if ((ledState ==LOW) && (currentMillis - previousMillis >= OffTime)){
      ledState = HIGH;
      previousMillis = currentMillis;
      digitalWrite(ledPin, ledState);

      
    }
  }
};

int greenPin = 9;
int yellowPin = 8;
int redPin = 7;
int buttonPin=2;

Flasher led1(greenPin,1000,2000,0);
Flasher led2(yellowPin,1000,2000,1000);
Flasher led3(redPin, 1000,2000,2000);


void setup() {
  
  // put your setup code here, to run once:
pinMode(buttonPin, INPUT_PULLUP);
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  
int value = digitalRead(buttonPin);
Serial.print(value);
if(value == 1){
  digitalWrite(greenPin, HIGH);
  digitalWrite(yellowPin, LOW);
  digitalWrite(redPin, LOW);

}else{
  
led1.Update();
led2.Update();
led3.Update();

}

}
