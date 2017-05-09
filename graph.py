#! /usr/bin/env python

from mpu6050 import mpu6050
import matplotlib.pyplot as plt

t = []
ax= []
ay = []
az = []
gx= []
gy = []
gz = []
global time
time = 0.00

plt.ion()

def read_data():
	sensor = mpu6050(0x68)
	ac = sensor.get_accel_data()
	gs = sensor.get_gyro_data()
	print ac
	print gs
	return ac, gs

def generate_graph(ac, gs):
	global time
	time += 0.01
	global t
	global ax, ay, az, gx, gy, gz
	t = t + [time]
	ax = ax + [ac['x']]
	ay = ay + [ac['y']]
	az = az + [ac['z']]
	gx = gx + [gs['x']]
	gy = gy + [gs['y']]
	gz = gz + [gs['z']]
	plt.figure(1)
	
	plt.subplot(211)
	plt.plot(t, ax)
	plt.ylabel("ACCEL-X")

	plt.subplot(212)
	plt.plot(t, az)
	plt.ylabel("ACCEL-Z")
	
	
	plt.show()
	plt.pause(2)

def main():
	while 1:
		accel, gyro = read_data()
		generate_graph(accel, gyro)
	
if __name__=="__main__":
	main()
