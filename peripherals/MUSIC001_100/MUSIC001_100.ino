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


#define time 200

void setup() {
  
pinMode(2,INPUT);//next
pinMode(3,INPUT);//play
pinMode(4,INPUT);//previous

pinMode(13,OUTPUT);//random led
pinMode(A1,INPUT);//volume

}

void loop() {
int s=0;
int n=0;
int p=0;

s=StopPlay(s);

if(digitalRead(4)==LOW && digitalRead(2)==HIGH)
  n=Next(n);


if(digitalRead(4)==HIGH && digitalRead(2)==LOW)
  p=Back(p);

Volume();

}//end loop


int StopPlay(int a)
{
  if(digitalRead(3)==HIGH && a==0)
{
    Serial.write("play\n");
    a=1;
}
  else if(digitalRead(3)==LOW && a==1)
          a=0;
return a;
}//end s&p

int Back(int p){
  if(digitalRead(4)==HIGH && p==0)
{
    Serial.write("back\n");
    p=1;
}
  else if(digitalRead(4)==LOW && p==1)
          p=0;
return p;
}

int Next(int n){
  if(digitalRead(2)==HIGH && n==0)
{
    Serial.write("next\n");
    n=1;
}
  else if(digitalRead(2)==LOW && n==1)
          n=0;
return n;
}


void Volume()
{
  int a=analogRead(4);
  Serial.write("Volume\n");
  Serial.println(a);
}
