#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
import time


# Manuel mode switch.
manuel = True

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize Ultrasonic Sensors.
us2 = UltrasonicSensor(Port.S1)
us = UltrasonicSensor(Port.S2)

# Initialize Motors.
motor = Motor(Port.A)

while manuel == True:
    while True:
        while us.distance() > 60:
            print("Top Distance:", us.distance())
            print("Bottom Distance:", us2.distance())
            print("Moving Up...")
            motor.run(-120)
            
        else:
            print("Platform detected. Stopping...")
            # Play a sound.
            ev3.speaker.beep()
            time.sleep(0.5)
            motor.hold()
            time.sleep(5)
            while us2.distance() > 60:
                print("Top Distance:", us.distance())
                print("Bottom Distance:", us2.distance())
                print("Moving Up...")
                motor.run(120)
            else:
                # Play a sound.
                ev3.speaker.beep()
                time.sleep(0.1)
                ev3.speaker.beep()
                time.sleep(0.1)
                motor.hold()
                time.sleep(5)
else:
    #Insert AI code here.
    print("test")
print("hello")