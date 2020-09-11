from time import time
from serial import Serial
from pythonCode import Sensor
portname = x
ser = Serial(portname, 115200, 8, 'N', 1, timeout=1)
def gyroValues():
    return (Sensor.getValues(ser))


