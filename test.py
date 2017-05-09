#! /usr/bin/env python

import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
from mpu6050 import mpu6050

GPIO.setwarnings(False)

accz = [[]]
gccz = [[]]
global time
global t
t = []
time = 0.00
plt.ion()

GPIO.setmode(GPIO.BOARD)
chan_list = [11, 13, 15]

GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)

def read_data():
	global a
	global g
	a = [0,0,0]
	g = [0,0,0]
	i = 0
	for i in range(0,3):
		GPIO.output(chan_list[i], GPIO.HIGH)
		sensor = mpu6050(0x69)
		a[i] = a[i] + sensor.get_accel_data()['z']
		g[i] = g[i] + sensor.get_gyro_data()['z']
		GPIO.output(chan_list[i], GPIO.LOW)
	return a, g
	
def generate_graph(ac, gc):
	global t, time
	time += 0.01
	t = t + [time]
	j = 0
	for j in range(0,3):
		accz[j] = accz[j] + [ac[j]]
		gccz[j] = gccz[j] + [gc[j]]
		plt.figure(j)
		plt.subplot(211)
		plt.plot(t, accz[j])
		plt.ylabel("ACCEL-Z")
		
		plt.subplot(212)
		plt.plot(t, gccz[j])
		plt.ylabel("GYRO-Z")
		plt.show()
	plt.pause(0.001)
		
		
def main():
	accel = []
	gyro = []
	while True:
		accel, gyro = read_data()
		generate_graph(accel, gyro)

if __name__=="__main__":
	main()
