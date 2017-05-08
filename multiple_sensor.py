#! /usr/bin/env python

import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
from mpu6050 import mpu6050

acc = [[]]
gcc = [[]]

plt.ion()

GPIO.setmode(GPIO.BOARD)
chan_list = [11, 13, 15]

GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)

def read_data():
	global a
	global g
	a = [[]]
	g = [[]]
	for i in range(3):
		GPIO.output(chan_list[i], GPIO.HIGH)
		sensor = mpu6050(0x69)
		a[i] = a[i] + sensor.get_accel_data()
		g[i] = g[i] + sensor.get_gyro_data()
		GPIO.output(chan_list[i], GPIO.LOW)
	return a, g
	
def generate_graph(a, g):
	global t, time
	time += 0.01
	t = t + [time]
	for i in range(3):
		accz[i] = accz[i] + [a[i]['z']]
		gccz[i] = gccz[i] + [g[i]['z']]
		plt.figure(i)
		plt.subplot(211)
		plt.plot(t, accz[i])
		plt.ylabel("ACCEL-Z")
		
		plt.subplot(212)
		plt.plot(t, gccz[i])
		plt.ylabel("GYRO-Z")
		
		
def main():
	accel = [[]]
	gyro = [[]]
	accel, gyro = read_data()
	generate_graph(accel, gyro)

if __name__=="__main__":
	main()
