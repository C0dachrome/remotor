#!/usr/bin/env python3
import os
import sys
import serial
import time
from adafruit_crickit import crickit

print("Remotor 0.1")
go = True

# Initialize DC motors on the CRICKIT board
motor_1 = crickit.dc_motor_1
motor_2 = crickit.dc_motor_2

if __name__ == '__main__':
    # Set up serial communication with the Arduino
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()
    
print("Press button 1 to begin")

# Configure a drive pin to act as a hardware reset for the Arduino
crickit.drive_1.frequency = 1000
crickit.drive_1.fraction = 1.0   # Resets Arduino through RESET pin
time.sleep(0.1)
crickit.drive_1.fraction = 0.0
ser.flushOutput()    # Clear serial output buffer

# Wait here until touch pad 1 is pressed
while crickit.touch_1.value == False:
    time.sleep(0.01)

# Pulse the reset pin again upon starting
crickit.drive_1.frequency = 1000
crickit.drive_1.fraction = 1.0
time.sleep(0.1)
crickit.drive_1.fraction = 0.0

# Main operation loop
while go:
    # Keep running until touch pad 4 is pressed to trigger a restart
    while crickit.touch_4.value == False:
        
        # Check if serial data is waiting from the Arduino
        if ser.in_waiting > 0:
            # Read and parse the first line for Motor 1
            line = ser.readline().decode('utf-8').strip()

            if float(line)*5 >= 1.0:
                motor_1.throttle = 0.9
            elif float(line)*5 <= -1.0:             
                motor_1.throttle = -0.9
            else:
                motor_1.throttle = float(line)*5

            print(float(line)*5)
            
            # Read and parse the next line for Motor 2
            line = ser.readline().decode('utf-8').rstrip()

            if float(line)*5 >= 1.0:
                motor_2.throttle = 0.9            
            elif float(line)*5 <= -1.0:
                motor_2.throttle = -0.9  
            else: 
                motor_2.throttle = float(line)*5

            print(float(line)*5)
            print(line)
            
    print("restarting!")
    # Cleanly restart this Python script using os.execv
    os.execv(sys.executable, ['remotor0_11.py'] + sys.argv)
    time.sleep(1)
    go = False
