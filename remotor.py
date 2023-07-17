#!/usr/bin/env python3
import serial
import time
from adafruit_crickit import crickit

print("Connecting to arduino serial..")

# make two variables for the motors to make code shorter to type
motor_1 = crickit.dc_motor_1
motor_2 = crickit.dc_motor_2

if __name__ == '__main__':
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
	ser.reset_input_buffer()
	print("Success!")

while True:
	if ser.in_waiting > 0:
		line = ser.readline().decode('utf-8').rstrip()
		motor_1.throttle = float(line)*3
		line = ser.readline().decode('utf-8').rstrip()
		motor_2.throttle = float(line)*3

		print(line)

