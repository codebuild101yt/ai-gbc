#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, InfraredSensor
from pybricks.parameters import Port
import time
from ev3_comm import EV3Server

# Initialize server.
server = EV3Server()

# Manual mode switch.
manual = True

# Initialize the EV3 Brick.
ev3 = EV3Brick()
outputdata = 0

# Initialize Ultrasonic Sensors.
us2 = InfraredSensor(Port.S1)
us = UltrasonicSensor(Port.S2)

# Initialize Motors.
motor = Motor(Port.A)

def non_blocking_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

if manual:
    while True:
        while us.distance() > 70:
            #print("Top Distance:", us.distance())
            #print("Bottom Distance:", us2.distance())
            #print("Moving Up...")
            motor.run(-500)
        else:
            #print("Platform detected. Stopping...")
            # Play a sound.
            ev3.speaker.beep()
            non_blocking_sleep(0.5)
            motor.hold()
            non_blocking_sleep(5)
            while us2.distance() >= 10:
                #print("Top Distance:", us.distance())
                #print("Bottom Distance:", us2.distance())
                #print("Moving Up...")
                motor.run(120)
            else:
                # Play a sound.
                ev3.speaker.beep()
                non_blocking_sleep(0.1)
                ev3.speaker.beep()
                non_blocking_sleep(0.1)
                motor.hold()
                non_blocking_sleep(5)
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
                non_blocking_sleep(1)
                print("auto fixing")
                non_blocking_sleep(1.5)
                data = "0"
            
            data = int(data)
            print("Recived data is: ", data)
            outputdata = 15 - data
            
            while us.distance() > 70:
                #print("Top Distance:", us.distance())
                #print("Bottom Distance:", us2.distance())
                #print("Moving Up...")
                motor.run(-320)
            else:
                #print("Platform detected. Stopping...")
                # Play a sound.
                ev3.speaker.beep()
                non_blocking_sleep(0.5)
                motor.hold()
                non_blocking_sleep(5)
                while us2.distance() >= 10:
                    #print("Top Distance:", us.distance())
                    #print("Bottom Distance:", us2.distance())
                    #print("Moving Up...")
                    motor.run(120)
                else:
                    # Play a sound.
                    ev3.speaker.beep()
                    non_blocking_sleep(0.1)
                    ev3.speaker.beep()
                    non_blocking_sleep(0.1)
                    motor.hold()
                    non_blocking_sleep(outputdata)
