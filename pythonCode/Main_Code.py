import time
from time import sleep
from pythonCode import maxSonarTTY
from pythonCode import motorController
from pythonCode import DataHolder
from pythonCode import Gyro

def main():
    timeInit = time.time()
    serialPort = "/dev/ttyAMA0"
    i = 0
    while True:
        i+1
        minDistane = 500
        maxDistance = 700
        #initial range in the rangediff equation
        rangeV0 = maxSonarTTY.measure(serialPort)
        #arbitrary sleep time... to be part of the nerual network equation
        sleep(.2)
        rangeV1 = maxSonarTTY.measure(serialPort)
        rangeDifference = rangeV1-rangeV0
        #creates a running total of gyro such that we can know current velocity.
        velocity = velocity + Gyro.gyroAccelX()
    #acceleration and decceleration logic
    #first if else is for maintaining x distance away from target vehicle
        #Final equation will look something like input = rangeDifference/Velocity/1000 will give us the current time to impact with the object. Now, assuming that we want there to be a legal 3 second gap we must adjust and make it input = (rangeDifference/Velocity/1000)-3(this number is arbitrary and will
        #based upon the acceleration curves we can test. Similarly for the max and min distances
        #Find the following methods in motorController.py
        if rangeV1 > maxDistance:
            motorController.motorAcceleration(abs(rangeV1-maxDistance))
        elif rangeV1 < minDistane:
            motorController.motorDecelleration(abs(rangeV1-minDistane))
        #this one is for keeping a constant distance from the object

        #Find the following methods in motorController.py
        if rangeDifference > 0:
            motorController.motorAcceleration(abs(rangeDifference/velocity/1000))
        elif rangeDifference < 0 :
            motorController.motorDecelleration(abs(rangeDifference/velocity/1000)

        #creates a file with the acceleration and the time of the robot. From there, we can derive the speed.
        file = open("data,txt", "w+")
        file.write("input line %d\r\n" %(i) +"data inputted: " %(Gyro.gyroAccelX()) +" time since start : " %(timeInit - time.time()))
            # arbitrary sleep time... to be part of the nerual network equation
    sleep(.5)

#Executes the code upon start
if __name__ == '__main__':
    main()
