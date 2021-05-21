

      

  





/*int ButtonValue =0;
int Button = 3;
int LED = 2;*/

const int a = 2; //constants that provide functionalities for pinMODE 
const int b = 3;
const int c = 4;
const int d = 5;
const int e = 6;
const int f = 7;
const int g = 8;
const int buttonPin = 13;  //here I'm supplying the constants associated with my buttons and buzzer
const int buttonPin2 = 1;
const int buzzer = A0;
//const int buttonPin3 = 2;



const int d1 = 9;  //Digit Constants
const int d2 = 10;
const int d3 = 11;
const int d4 = 12;

long n = 0000; //start time 
int x = 100; //
int del = 55; //roughly the delay time for 1 microsecond

int buttonstate = 0; //value of input to read buttons state
int buttonstate2 = 0;

//int buttonState3 = 0;  
 
 void setup(){
  
  pinMode(d1, OUTPUT); //Provides output for all digits and their attributes
  pinMode(d2, OUTPUT);
  pinMode(d3, OUTPUT);
  pinMode(d4, OUTPUT);
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(f, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(buttonPin, INPUT); //reads in input
  pinMode(buttonPin2, INPUT);
  pinMode(buzzer, INPUT);
   //pinMode(buttonPin3,INPUT);

  
  

//digitalRead(buttonPin3);
//onoff(buttonState3);
}


/*void onoff(int buttonState3){ //attemp at on/off swtich //attempt to make an on/off button
  //digitalRead(buttonPin3);
  if (buttonState3==HIGH){    
    int ok = 1;
  }else{
      onoff(buttonState3);
  }
}*/

  
 
void loop(){
  buttonstate = digitalRead(buttonPin); //if button is not pressed then run as normal
  if(buttonstate == HIGH){ //interprets buttonstate
  pinMode(d1, OUTPUT); //Provides output for all digits and segments
  pinMode(d2, OUTPUT);
  pinMode(d3, OUTPUT);
  pinMode(d4, OUTPUT);
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(f, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buzzer, INPUT);
 
  clearLEDs(); // This is to prevent all the pins extending output to digits, they must clear first before a new number can be displayed
  pickDigit(1); //makes speicif digit low to ensure it can be changed based on new parameters
  pickNumber((n/x/1000)%10); //n is interpreted, which will be 0 for all the digits until n reach 1001
  delayMicroseconds(del); //Must have a small delay to make sure clock counts correctly, else it will count too fast
  clearLEDs(); 
  pickDigit(2);
  pickNumber((n/x/100)%10); //etc
  delayMicroseconds(del);
  clearLEDs();//
  pickDigit(3);
  //dispDec(3);
  pickNumber((n/x/10)%10); //10001, first digit get displayed
  delayMicroseconds(del);
  clearLEDs();
  pickDigit(4);
  pickNumber(n/x%10); //when n is 1001, first digit gets displayed
  delayMicroseconds(del);


 
  n++; // counts up
 
  if (digitalRead(13) == LOW )  //restart if button is pressed
  {
    n = 0000; //restart time once display reaches 9999
  }


  


}else{ //reset button is executed 
  pinMode(buzzer, OUTPUT); //commands output to buzzer
  digitalWrite(buzzer, HIGH); //makes buzzer go off
  
  tone(buzzer, 250); //pitch of buzzer


  
  digitalWrite(d1, LOW); // Displays output of all digits, from assigned const values
  digitalWrite(d2, LOW);
  digitalWrite(d3, LOW);
  digitalWrite(d4, LOW);
  pinMode(d1, LOW); //Provides output for all digits and their attributes
  pinMode(d2, LOW);
  pinMode(d3, LOW);
  pinMode(d4, LOW);
  pinMode(a, LOW);
  pinMode(b, LOW);
  pinMode(c, LOW);
  pinMode(d, LOW);
  pinMode(e, LOW);
  pinMode(f, LOW);
  pinMode(g, LOW);
  
}


buttonstate2 = digitalRead(buttonPin2); //buzzer and functions for pause button
if(buttonstate2 == LOW){
  pinMode(buzzer, OUTPUT); //commands output to buzzer
  digitalWrite(buzzer, HIGH); //makes buzzer go off
  
    tone(buzzer, 250); //pitch of buzzer
  pinMode(a, LOW); //all segments temporarily go low
  pinMode(b, LOW);
  pinMode(c, LOW);
  pinMode(d, LOW);
  pinMode(e, LOW);
  pinMode(f, LOW);
  pinMode(g, LOW);
  delay(500);
}

}
 
void pickDigit(int x) //selects digit to be changed
{
  digitalWrite(d1, HIGH); // Displays blank output of all digits, from their assigned constant values
  digitalWrite(d2, HIGH);
  digitalWrite(d3, HIGH);
  digitalWrite(d4, HIGH);
 
  switch(x) //
  {
  case 1:  //
    digitalWrite(d1, LOW); //if 1 is selected d1 goes low, then pickNumber() is selected next.  The digit must go low before it can change otherwise the digit will not change correctly
    break; //
  case 2: 
    digitalWrite(d2, LOW); 
    break;
  case 3: 
    digitalWrite(d3, LOW);
    break;
  default: 
    digitalWrite(d4, LOW); 
    break;
  }
}
void pickNumber(int x) //responsible for changing value of digit
{
  switch(x) //Because the input is the result of (a number) being % 10, then whatever that number may be, it gets called and it's corresponding method gets called,
            // if the result was 1, then one() gets called and the number one is displayed
  {
  default: 
    zero(); 
    break;
  case 1: 
    one(); 
    break;
  case 2: 
    two(); 
    break;
  case 3: 
    three(); 
    break;
  case 4: 
    four(); 
    break;
  case 5: 
    five(); 
    break;
  case 6: 
    six(); 
    break;
  case 7: 
    seven(); 
    break;
  case 8: 
    eight(); 
    break;
  case 9: 
    nine(); 
    break;
  }
}
 

 
void clearLEDs()//
{
  digitalWrite(a, LOW);
  digitalWrite(b, LOW);
  digitalWrite(c, LOW);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  digitalWrite(g, LOW);
  
}
 
void zero()  // 
{
  digitalWrite(a, HIGH);
  digitalWrite(b, HIGH);
  digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);
  digitalWrite(e, HIGH);
  digitalWrite(f, HIGH);
  digitalWrite(g, LOW);
}
 
void one()
{
  digitalWrite(a, LOW);
  digitalWrite(b, HIGH);
  digitalWrite(c, HIGH);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  digitalWrite(g, LOW);
}
 
void two()
{
  digitalWrite(a, HIGH);
  digitalWrite(b, HIGH);
  digitalWrite(c, LOW);
  digitalWrite(d, HIGH);
  digitalWrite(e, HIGH);
  digitalWrite(f, LOW);
  digitalWrite(g, HIGH);
}
 
void three()
{
  digitalWrite(a, HIGH);
  digitalWrite(b, HIGH);
  digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  digitalWrite(g, HIGH);
}
 
void four()
{
  digitalWrite(a, LOW);
  digitalWrite(b, HIGH);
  digitalWrite(c, HIGH);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, HIGH);
  digitalWrite(g, HIGH);
}
 
void five()
{
  digitalWrite(a, HIGH);
  digitalWrite(b, LOW);
  digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);
  digitalWrite(e, LOW);
  digitalWrite(f, HIGH);
  digitalWrite(g, HIGH);
}
 
void six()
{
  digitalWrite(a, HIGH);
  digitalWrite(b, LOW);
  digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);
  digitalWrite(e, HIGH);
  digitalWrite(f, HIGH);
  digitalWrite(g, HIGH);
}
 
void seven()
{
  digitalWrite(a, HIGH);
  digitalWrite(b, HIGH);
  digitalWrite(c, HIGH);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  digitalWrite(g, LOW);
}
 
void eight()
{
  digitalWrite(a, HIGH);
  digitalWrite(b, HIGH);
  digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);
  digitalWrite(e, HIGH);
  digitalWrite(f, HIGH);
  digitalWrite(g, HIGH);
}
 
void nine()
{
  digitalWrite(a, HIGH);
  digitalWrite(b, HIGH);
  digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);
  digitalWrite(e, LOW);
  digitalWrite(f, HIGH);
  digitalWrite(g, HIGH);
}
    
