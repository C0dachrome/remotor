> [PROJECT STATUS - ARCHIVED/UNMAINTAINED]

# remotor
Drive DC motors from an RC reciever with Arduino and Raspberry Pi + Adafruit CRICKIT HAT.

Tested on an Arduino Uno, Raspberry pi 3b running raspberry pi OS lite, with an adafruit CRICKIT HAT, flysky fs-gr3e reciever and flysky fs-gt3b radio.

WIP, not fully functional.

start the program with 
```
python ./forever.py remotor0_21.py
```
## Connection information:

CH 1 signal -----> pin 11 arduino
CH 2 signal -----> pin 10 arduino
reviever Vcc ----> 5v on arduino
reviever GND ----> GND on arduino

arduino RESET ----> drive 1 on CRICKET HAT (not currently being used)

Arduino -----> raspsberry pi 3b via USB (im assuming you can use the UART GPIOs on the pi too)

Motors 1 & 2 -----> motor 1 & 2 outputs on CRICKET HAT




