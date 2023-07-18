#!/usr/bin/env python3
import os
import sys
import serial
import time
from adafruit_crickit import crickit

print("Remotor 0.1")
go  = True

motor_1 = crickit.dc_motor_1
motor_2 = crickit.dc_motor_2

if __name__ == '__main__':
	ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
	ser.reset_input_buffer()
print("Press button 1 to begin")

crickit.drive_1.frequency = 1000

crickit.drive_1.fraction = 1.0   # resets arduino through RESET pin
time.sleep(0.1)
crickit.drive_1.fraction = 0.0
ser.flushOutput()    #not sure if this works but it should clear the serial console??

while crickit.touch_1.value == False:

	time.sleep(0.01)



crickit.drive_1.frequency = 1000
crickit.drive_1.fraction = 1.0
time.sleep(0.1)
crickit.drive_1.fraction = 0.0

while go:
	while crickit.touch_4.value == False:
		

		if ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').strip() # read serial

			if float(line)*5 >= 1.0:
				motor_1.throttle = 0.9
			elif float(line)*5 <= -1.0:               # set motor1 throttle accordingly
				motor_1.throttle = -0.9
			else:
				motor_1.throttle = float(line)*5

			print(float(line)*5)
			line = ser.readline().decode('utf-8').rstrip() # read serial

			if float(line)*5 >= 1.0:
				motor_2.throttle = 0.9			# set motor2 throttle accordingly
			elif float(line)*5 <= -1.0:
				motor_2.throttle = 0.9
			else: 
				motor_2.throttle = float(line)*5

			print(float(line)*5)
			print(line)
	print("restarting!")
	os.execv(sys.executable, ['remotor0_11.py'] + sys.argv)
	time.sleep(1)
	go = False

