#include <math.h>

// PER LCD: http://www.maffucci.it/2012/02/17/appunti-su-arduino-pilotare-un-display-lcd/

char buffer[100];

double Thermistor(int RawADC) {
 double Temp;
 Temp = log(10000.0*((1024.0/RawADC-1))); 
 Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp ))* Temp );
 Temp = Temp - 273.15;           
 return Temp;
}

void setup() {
 Serial.begin(9600);
 Serial.write("start\n");
}

void loop() {
  String command = readCommand();
  if (command.length() > 1)
    executeCommand(command);
}

void executeCommand(String command) {
  //sprintf(buffer, "Got command %s\n", command.c_str());
  //Serial.write(buffer);
  if(command == "temperature")
    sendTemperature();
  else if (command == "info")
    sendInfo();
  else {
    sprintf(buffer, "unrecognized_command %s\n", command.c_str());
    Serial.write(buffer);
  }
}

String readCommand() {
  Serial.write("#");
  String command = "";
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

void sendTemperature() {
  int val = analogRead(0);
  for(int i=0; i < 2; i++){
    val=(val+analogRead(0))/2;
  }
  double temp = Thermistor(val);
  Serial.print("temperature ");
  Serial.println(temp);
}

void sendInfo() {
  Serial.write("info TEMP001 100\n");
}

