#!/usr/bin/env python3
import serial
import time
from adafruit_crickit import crickit

print("Remotor 0.1")


motor_1 = crickit.dc_motor_1
motor_2 = crickit.dc_motor_2

if __name__ == '__main__':
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
	ser.reset_input_buffer()

while True:
	if ser.in_waiting > 0:
		line = ser.readline().decode('utf-8').rstrip()
		if float(line)*5 >= 1.0:
			motor_1.throttle = 0.9
		elif float(line)*5 <= -1.0:
			motor_1.throttle = -0.9
		else:
			motor_1.throttle = float(line)*5

		print(float(line)*5)
		line = ser.readline().decode('utf-8').rstrip()

		if float(line)*5 >= 1.0:
			motor_2.throttle = 0.9
		elif float(line)*5 <= -1.0:
			motor_2.throttle = 0.9
		else: 
			motor_2.throttle = float(line)*5

		print(float(line)*5)
		print(line)

