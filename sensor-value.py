#! /usr/bin/env python
from mpu6050 import mpu6050
import math

sensor = mpu6050(0x68)

while 1:
    acc_data = sensor.get_accel_data()
    ax = acc_data['x']
    ay = acc_data['y']
    az = acc_data['z']
    print 'accelerometer : ', acc_data
    gyro_data = sensor.get_gyro_data()
    gx = gyro_data['x']
    gy = gyro_data['y']
    gz = gyro_data['z']
    print 'gyroscope : ',gyro_data
    roll = math.atan2(-ay,az)
    pitch = math.atan2(ax, math.sqrt(ay ** 2 + az ** 2))
    print 'pitch : ', pitch
    print 'roll : ', roll

