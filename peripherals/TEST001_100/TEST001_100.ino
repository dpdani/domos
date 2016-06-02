#include <stdio.h>

char buffer[100];
String inputString = "";
boolean stringComplete = false;

void setup() {
  pinMode(7, INPUT);    //button luce
  pinMode(8, INPUT);    //button porta
  pinMode(14,OUTPUT);    //check luce
  
  pinMode(13, OUTPUT);  //led allarme
  pinMode(9, OUTPUT);   //buzzer allarme

  pinMode(12, OUTPUT);  //led lampada
  pinMode(11, OUTPUT);  //led luce
  pinMode(10, OUTPUT);  //led pc
  
  Serial.begin(9600);
  Serial.write("start\n");

}
int d=0;

void loop() {
 
  Serial.write("starting loop...\n");
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
  Serial.write("salve\n");
  // supposes serial to be available
  String command = "";
  while(1)
  while(Serial.available()>0) {//Serial.available
    //Serial.write("Waiting for command...\n");
    char c = (char)Serial.read();
    Serial.write(c);
    if(c == '\n')
      return command;
   if (int(c) != 255 || c != '\xff')
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
    if(digitalRead(8)==HIGH)
       {
         digitalWrite(14,HIGH);
       return 1;
       }
    else {
       digitalWrite(14,LOW);
       return 0;
    }
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

void info() {
 Serial.write("info TEST001 100\n");
}  
