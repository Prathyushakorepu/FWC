#include <Arduino.h>:
int A=1,B=1;
int x0,x1,x2,x3;
int Q; 
void setup() 
{
    pinMode(2, OUTPUT);              
}
void loop() 
{
x0=(!A);
x1=(!B);
x2=(!((x0) || (x1)));
x3=(!((A) || (B)));
Q=(!((x2) || (x3)));
digitalWrite(2,Q);
}
