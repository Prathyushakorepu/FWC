//XOR USING NOR GATES
#include <avr/io.h>
#include <stdbool.h>
 
int main (void)
{
   bool x0,x1,x2,x3,Q;
   bool a=1,b=0;

   DDRD=0b00000100;   //declaring pin 2 as output pin in portD
   DDRB=0b11111100;   //dlclaring pins 0 and 1 of portB as inputs

 //Equations
   x0=(!a);
   x1=(!b);
   x2=(!((x0) || (x1)));
   x3=(!((a) || (b)));
   Q=(!((x2) || (x3)));
//Giving Q to pin 2 of PORTD
     PORTD=(Q << 2);

      return 0;

}
