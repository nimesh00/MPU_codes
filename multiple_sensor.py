#! /usr/bin/env python

import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
from mpu6050 import mpu6050
import numpy as np
q = 0
r = 0
accx = [[] for q in range(3)]
gccx= [[] for r in range(3)]
q = 0
r = 0
accy = [[] for q in range(3)]
gccy= [[] for r in range(3)]
q = 0
r = 0
accz = [[] for q in range(3)]
gccz= [[] for r in range(3)]

plt.ion()

GPIO.setmode(GPIO.BOARD)
chan_list = [11, 13, 15]
GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)

global time
time = 0.00
t = []

def read_data():
	global a
	global g
	q = 0
	r = 0
	a = [[] for q in range(3)]
	g = [[] for r in range(3)]
	for i in range(3):
		GPIO.output(chan_list[i], GPIO.HIGH)
		sensor = mpu6050(0x69)
		a[i] = a[i] + [sensor.get_accel_data()]
		g[i] = g[i] + [sensor.get_gyro_data()]
		GPIO.output(chan_list[i], GPIO.LOW)
	#print a
	#print g
	return a, g
	
def generate_graph(a, g):
	global time
	time += 0.01
	global t
	t = t + [time]
	for i in range(3):
		accx[i] = accx[i] + [a[i][0]['x']]
		gccx[i] = gccx[i] + [g[i][0]['x']]
		accy[i] = accy[i] + [a[i][0]['y']]
		gccy[i] = gccy[i] + [g[i][0]['y']]
		accz[i] = accz[i] + [a[i][0]['z']]
		gccz[i] = gccz[i] + [g[i][0]['z']]
		#print 'Accelerometer:', accx[i], '---', accy[i], '---', accz[i]
		#print 'gyroscope: ', gccx[i], '---', gccy[i], '---', gccz[i]
		#print 'T: ', t
		plt.figure(1)
		plt.subplot(211)
		plt.plot(t, accx[i])
		plt.ylabel("ACCELERATION")
		
		plt.subplot(212)
		plt.plot(t, gccx[i])
		plt.ylabel("GYROSCOPIC DATA")
	plt.show()
	#plt.pause(0.001)	
		
def main():
	q = 0
	r = 0
	accel = [[] for q in range(3)]
	gyro = [[] for r in range(3)]
	while True:
		accel, gyro = read_data()
		generate_graph(accel, gyro)

if __name__=="__main__":
	main()
