//Turns LED on and off
#include <avr/io.h>
//#include <util/delay.h>
#include <stdbool.h>
 
int main (void)
{
   bool x0,x1,x2,x3,Q;
   bool a=1,b=0;

   DDRD=0b00000100;
   DDRB=0b11111100;

   x0=(!a);
   x1=(!b);
   x2=(!((x0) || (x1)));
   x3=(!((a) || (b)));
   Q=(!((x2) || (x3)));

     PORTD=(Q << 2);

      return 0;

}
