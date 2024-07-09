#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
import time
import ev3_comm
from ev3_comm import EV3Server

# Initialize server.
server = EV3Server()

# Manual mode switch.
manual = False

# Initialize the EV3 Brick.
ev3 = EV3Brick()
outputdata = 0

# Initialize Ultrasonic Sensors.
us2 = UltrasonicSensor(Port.S1)
us = UltrasonicSensor(Port.S2)

# Initialize Motors.
motor = Motor(Port.A)

if manual:
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
    if __name__ == "__main__":
        server.wait_for_connection()  # Blocks until a client connects
        
        # Execution continues after a client connects
        print("Connected to client, ready to receive and send data.")
        
        while True:
            data = server.receive_message()
            print("Data received:", data)
            # Further processing of received data

            if data is None:
                print("no received data")
                time.sleep(1)
                print("auto fixing")
                time.sleep(1.5)
                data = "0"
            
            data = int(data)
            
            outputdata = 15-data
            
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
                    time.sleep(outputdata)
                    outputdata = 0
            
