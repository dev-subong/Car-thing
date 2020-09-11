#!/usr/bin/python3
# Filename: rangeFind.py

# sample script to read range values from Maxbotix ultrasonic rangefinder
import time
from time import sleep
from pythonCode import maxSonarTTY
from pythonCode import motorController
from pythonCode import DataHolder
from pythonCode import Gyro

def main():
    timeInit = time.time()
    serialPort = "/dev/ttyAMA0"
    minDistane = 500
    maxDistance = 700
    i = 0
    while True:
        i+1
        rangeV0 = maxSonarTTY.measure(serialPort)
        sleep(.2)
        rangeV1 = maxSonarTTY.measure(serialPort)
        rangeDifference = rangeV1-rangeV0

    #acceleration and decceleration logic
    #first if else is for maintaining x distance away from target vehicle
        if rangeV1 > maxDistance:
            motorController.motorAcceleration(abs(rangeV1-maxDistance))
        elif rangeV1 < minDistane:
            motorController.motorDecelleration(abs(rangeV1-minDistane))
        #this one is for keeping a constant distance from the object
        if rangeDifference > 0:
            motorController.motorAcceleration(abs(rangeDifference))
        elif rangeDifference < 0 :
            motorController.motorDecelleration(abs(rangeDifference))
        #creates a file that will hold gyro data to fine tune the motor
        file = open("data,txt", "w+")
        file.write("input line %d\r\n" %(i) +"data inputted: " %(Gyro.gyroValues()) +" time since start : " %(timeInit - time.time()))