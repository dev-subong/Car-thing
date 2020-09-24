from time import time
import time
import board
import busio
import adafruit_lsm9ds1
from serial import Serial
from pythonCode import Sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

#Methods for acceleration values
def gyroValuesAccelX():
    accel_x, accel_y, accel_z = sensor.acceleration
    return (accel_x)
def gyroValuesAccelY():
    accel_x, accel_y, accel_z = sensor.acceleration
    return (accel_y)
def gyroValuesAccelZ():
    accel_x, accel_y, accel_z = sensor.acceleration
    return (accel_Z)
def gyroValuesAccel():
    accel_x, accel_y, accel_z = sensor.acceleration
    return (accel_x, accel_y, accel_z)


