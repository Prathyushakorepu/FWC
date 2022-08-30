.include "/home/prathyusha/prathyusha/m328Pdef.inc"
ldi r16,0b00000100            ;identifying output  pin 2
out DDRD,r16
ldi r17,0b11111100            ;identifying input pins 8,9
out DDRB,r17
ldi r17,0b11111101            ;giving input
out PortB,r17

ldi r18,0b00000001
ldi r19,0b00000001

AND r18,r17                   ;r18   (B)
LSR r17
AND r19,r17                   ;r19   (A)

ldi r20,0b00000001
eor r20,r18                   ;r20=B'(x1)

ldi r21,0b00000001
eor r21,r19                   ;r21=A'(x0)

OR r21,r20                    ;r21=x0+x1  

ldi r22,0b00000001
eor r22,r21                   ;r22=(x0+x1)'(x2)

OR r18,r19                    ;r18=A+B

ldi r23,0b00000001
eor r23,r18                   ;r23=(A+B)'  (x3)

OR r22,r23                     ;r22=x2+x3

ldi r24,0b00000001
eor r24,r22                   ;r24         (Q)

LSL r24
LSL r24

mov r16,r24

out PortD,r16

start:
rjmp start
