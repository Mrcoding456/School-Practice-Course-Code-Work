const int LED= 9; 

// define LED for Pin 9

void setup(){
  
  pinMode(LED, OUTPUT); // Set the LED pin as an output
  
  }
  void loop(){ 
    digitalWrite(LED, HIGH); //Turn on
    delay(1000);
    digitalWrite(LED, LOW);  //Turn off
    delay(1000);
    
}
