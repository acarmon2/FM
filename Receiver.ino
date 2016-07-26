#include <JeeLib.h>
#include <Ports.h>
#include <RF12.h>

void setup () {
  rf12_initialize('R', RF12_433MHZ, 88);
  Serial.begin(9600);
}

void loop () {
  if (rf12_recvDone()) {
    for(int x = 0; x < rf12_len; x++){
      Serial.print(rf12_data[x]);
      Serial.print(" ");
    }
  delay(500);
  Serial.println();
  }
}
