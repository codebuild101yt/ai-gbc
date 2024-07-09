#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port

# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

us = UltrasonicSensor(Port.S2)

print(us.distance())