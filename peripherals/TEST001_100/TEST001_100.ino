#include <stdio.h>

char buffer[100];
String inputString = "";
boolean stringComplete = false;

void setup() {
  pinMode(7, INPUT);    //button luce
  pinMode(8, INPUT);    //button porta
  
  pinMode(13, OUTPUT);  //led allarme
  pinMode(9, OUTPUT);   //buzzer allarme

  pinMode(12, OUTPUT);  //led lampada
  pinMode(11, OUTPUT);  //led luce
  pinMode(10, OUTPUT);  //led pc
  
  Serial.begin(9600);
  Serial.write("start\n");

}
int d=0;
int z=0;
int y=0;
void loop() {
    String command = readCommand();
    if(command.length() > 1)
    executeCommand(command);
  /*if (stringComplete) {
    Serial.println(inputString);
    inputString = "";
    stringComplete = false;
  }*/
}


void executeCommand(String command) {
  Serial.write("kakaak\n");
  //sprintf(buffer, "Got command %s\n", command.c_str());
  //Serial.write(buffer);
  if (command == "toggle_led") {
    MakeItShine();
    Serial.write("done.\n");
  }
  else if (command == "read_button") {
    int b = Button();
    sprintf(buffer, "button_is %d\n", b);
    Serial.write(buffer);
  }
  else if (command== "info")
    info();
  /*else if(command=="asfasdfafa")
  {
   Intruder();
   sprintf(buffer,"");
   Serial.write(buffer);
  }*/
  else {
    sprintf(buffer, "unrecognized_command %s\n", command.c_str());
    Serial.write(buffer);
  }
}


String readCommand() {
  // supposes serial to be available
  String command = "";
  doorCheck();
  while(Serial.available()>0) {//Serial.available
    //Serial.write("Waiting for command...\n");
    char c = (char)Serial.read();
    Serial.write(c);
    if(c == '\n')
      return command;
   if (int(c) <= 125 || int(c) >= 32)
      command += c;
  }
}




/*void serialEvent() {
  while(Serial.available()) {
    char inChar = (char) Serial.read();
    inputString += inChar;
    if(inChar == '\n')
      stringComplete = true;
  }
}
*/
int Button(){
    if(digitalRead(7)==HIGH && y==0)
       {
         Serial.write("button_pressed\n");
         y=1;
       }
         
    else if(digitalRead(7)==LOW && y==1)
       {
         y=0;
       }
    return y;
  }
  

void MakeItShine(){
  if(d==1){
    digitalWrite(11,LOW);
    d=0;
    }
  else if(d==0){
    digitalWrite(11,HIGH);
    d=1;
}}

void Intruder(){
  digitalWrite(11,HIGH);
 while(readCommand()!=""){
  tone(9,4000);
  delay(500);
  noTone(9);
}
}
void doorCheck(){
if(digitalRead(8)==LOW && z==0){
Serial.write("door_opened\n");
z=1;
}
else if(digitalRead(8)==HIGH && z==1){
Serial.write("door_closed\n");
z=0;
}
}

void info() {
 Serial.write("info TEST001 100\n");
}  
