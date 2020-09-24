##Controls the DC motors
#library that allows the motors to function
from adafruit_motorkit import MotorKit

kit = MotorKit()
def motorAcceleration(distanceQuantity):
    #Acceleration for motor 1 and 2
    kit.motor1.throttle= distanceQuantity
    kit.motor2.throttle = distanceQuantity

def motorDecelleration(distanceQuantity):
    #Deceleration for motor 1 and 2
    kit.motor1.throttle = distanceQuantity
    kit.motor2.throttle = distanceQuantity