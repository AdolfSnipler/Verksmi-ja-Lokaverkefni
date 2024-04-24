#include <Servo.h>
#include <VexMotor.h>

Servo munnur;         // Servo mótorinn sem stjórnar hreyfingunni í munninum er hérna kallaður "munnur"
Servo haus;           // Servo mótorinn sem stjórnar hreyfingunni á hausnum er hérna kallaður "haus"
VexMotor likami;      // Vex mótorinn sem hreyfir líkaman er hérna kallaður "likami"

int pos = 110;      // setur munninn í upphafsstöðu
int inputPin = 8;   // setur PIR hreyfiskynjarann í digital port 8
int pirState = LOW; // we start, assuming no motion detected
int val = 0;        // variable for reading the pin status
 
void setup() {
  pinMode(inputPin, INPUT);     // declare sensor as input


  munnur.attach(9);  // setur munn mótorinn í digital port 9
  haus.attach(11);   // setur haus mótorinn í digital port 11

  likami.set(10);   // setur Vex mótorinn í digital port 10
  Serial.begin(9600);
}
 
void loop(){
  val = digitalRead(inputPin);  // read input value

  if (val == HIGH)  // check if the input is HIGH
  {

    if (pirState == LOW) 
  {
      Serial.println("Motion detected!"); // print on output change
      pirState = HIGH;

      // Vex mótorinn
      
      likami.set(57); // setur mótorinn af stað í hraða 57
      delay(4510);    // mótorinn keyrir í 4,51 sek
      likami.set(0);  // stoppar mótorinn
      delay(500);     // bíður í hálfa sek
    
      
      // Hreyfing á stóra servo til að hreyfa hausinn til hliðar
    
      for (pos = 100; pos >= 60; pos -= 1) {  // fer frá 100 gráðum í 60 gráður
        haus.write(pos);                      // segir mótorinum að fara í stöðu eftir breytunni 'pos'
        delay(15);                            // bíður ú 15 ms eftir mótorinum að fara í stöðuna
      }
      for (pos = 60; pos <= 130; pos += 1) {  // fer frá 60 gráðum í 130 gráður, 1 gráða í einu
        haus.write(pos);                      // ---||---
        delay(15);                            // ---||---
      }
      for (pos = 130; pos >= 60; pos -= 1) {  // fer frá 130 gráðum í 60 gráður, 1 gráða í einu
        haus.write(pos);                      // ---||---
        delay(15);                            // ---||---
      }
      for (pos = 60; pos <= 130; pos += 1) {  // fer frá 60 gráðum í 130 gráður, 1 gráða í einu
        haus.write(pos);                      // ---||---
        delay(15);                            // ---||---
      }
      for (pos = 130; pos >= 60; pos -= 1) {  // fer frá 130 gráðum í 60 gráður, 1 gráða í einu
        haus.write(pos);                      // ---||---
        delay(15);                            // ---||---
      }
      for (pos = 60; pos <= 100; pos += 1) {  // fer frá 60 gráðum í 100 gráður, 1 gráða í einu
        haus.write(pos);                      // ---||---
        delay(15);                            // ---||---
      }
      delay(500);                             //  bíður í hálfa sek
    
    
        // Hreyfing á litla bláa servo til að opna og loka munn
    
      for (pos = 110; pos <= 150; pos += 1) {  // fer frá 110 gráðum í 150 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
      for (pos = 150; pos >= 110; pos -= 1) {  // fer frá 150 gráðum í 110 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
      for (pos = 110; pos <= 150; pos += 1) {  // fer frá 110 gráðum í 150 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
      for (pos = 150; pos >= 110; pos -= 1) {  // fer frá 150 gráðum í 110 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
      for (pos = 110; pos <= 150; pos += 1) {  // fer frá 110 gráðum í 150 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
      for (pos = 150; pos >= 110; pos -= 1) {  // fer frá 150 gráðum í 110 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
      for (pos = 110; pos <= 150; pos += 1) {  // fer frá 110 gráðum í 150 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
      for (pos = 150; pos >= 110; pos -= 1) {  // fer frá 150 gráðum í 110 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
      for (pos = 110; pos <= 150; pos += 1) {  // fer frá 110 gráðum í 150 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
       for (pos = 150; pos >= 110; pos -= 1) { // fer frá 150 gráðum í 110 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
      for (pos = 110; pos <= 150; pos += 1) {  // fer frá 110 gráðum í 150 gráður, 1 gráða í einu
        munnur.write(pos);                     // ---||---
        delay(15);                             // ---||---
      }
    }
  } 
  else 
  {
    
    if (pirState == HIGH)
  {
      Serial.println("Motion ended!");  // print on output change
      pirState = LOW;
    }
  }
}
