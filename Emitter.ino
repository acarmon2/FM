#include <JeeLib.h>
#include <Ports.h>
#include <RF12.h>

byte OutData, Pending;
char cont;
//char Data[3] = {0x13, 0x17, 0x25};
char Data[] = {};
MilliTimer sendTimer;
char a;

void setup(){
  rf12_initialize('T', RF12_433MHZ, 88);
  Serial.begin(9600);
  cont = 1;
}

void loop(){
  rf12_recvDone();

  if(rf12_canSend()){
    rf12_sendStart(0, &Data, sizeof Data);
  }
  //Data[3] = cont + 1;
  delay(30);
}
