# remotor
 drive motors and servos from an rc reciever with arduino and raspberry pi with adafruit CRICKIT HAT.

Tested on an Arduino Uno, Raspberry pi 3b running raspberry pi OS lite, with an adafruit CRICKIT HAT.

WIP, not fully functional.

start the program with 
python ./forever.py remotor0_21.py



Bugs

remotor.py does not start reliably, assuming because the arduino starts communicating as soon as its powered on. Add bidirectional serial communication. Initiate the arduino code via serial. --- FIXED-ish worked around the problem by adding forever.py which restarts the code when an error occurs.


