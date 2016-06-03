/*    Copyright (C) 2016  Domos Group
 *
 *    This program is free software: you can redistribute it and/or modify
 *    it under the terms of the GNU General Public License as published by
 *    the Free Software Foundation, either version 3 of the License, or
 *    (at your option) any later version.
 *
 *    This program is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *    along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */


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
  while(Serial.available()>0) {
    char c = (char)Serial.read();
    Serial.write('?');
    if(c == '\n') {
      Serial.write('\n');
      return command;
    }
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

