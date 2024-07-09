## Port Connections Documentation

### Overview

This document provides a detailed guide on the port connections for the LEGO Mindstorms EV3 setup used in the script. Follow these instructions to correctly connect the sensors and motor to the EV3 Brick.

### Port Assignments

1. **Ultrasonic Sensor 1 (Top Sensor)**
   - **Port:** S1
   - **Component:** Ultrasonic Sensor
   - **Purpose:** Measures distance from the top part of the robot.
   - **Connection:** Plug the Ultrasonic Sensor into port S1 on the EV3 Brick.

2. **Ultrasonic Sensor 2 (Bottom Sensor)**
   - **Port:** S2
   - **Component:** Ultrasonic Sensor
   - **Purpose:** Measures distance from the bottom part of the robot.
   - **Connection:** Plug the Ultrasonic Sensor into port S2 on the EV3 Brick.

3. **Motor**
   - **Port:** A
   - **Component:** Large Motor
   - **Purpose:** Controls the movement of the platform (up and down).
   - **Connection:** Plug the Large Motor into port A on the EV3 Brick.

### Script Initialization

The script initializes the components with the assigned ports as follows:

```python
# Initialize Ultrasonic Sensors.
us2 = UltrasonicSensor(Port.S1)
us = UltrasonicSensor(Port.S2)

# Initialize Motors.
motor = Motor(Port.A)
```

### Setup Instructions

1. **Connecting Ultrasonic Sensor 1 (Top Sensor):**
   - Take the Ultrasonic Sensor and connect it to port S1 on the EV3 Brick.
   - This sensor will measure distances from the top part of your robot setup.

2. **Connecting Ultrasonic Sensor 2 (Bottom Sensor):**
   - Take the second Ultrasonic Sensor and connect it to port S2 on the EV3 Brick.
   - This sensor will measure distances from the bottom part of your robot setup.

3. **Connecting the Motor:**
   - Connect the Large Motor to port A on the EV3 Brick.
   - This motor will be responsible for moving the platform up and down based on sensor readings or remote commands.

### Running the Script

Ensure that the sensors and motor are connected to the correct ports before running the script. The script will control the motor's movements based on the distance readings from the ultrasonic sensors or commands received from a remote client.

- **Manual Mode:** Set the `manual` variable to `True` in the script to operate the motor manually based on the sensor readings.
- **Automated Mode:** Set the `manual` variable to `False` in the script to operate the motor based on remote commands received through the `EV3Server`.

By following these port connections and setup instructions, you can ensure that your EV3 Brick and components are correctly configured for the script's operations.
