# EV3 Mindstorms Project

This project involves controlling a LEGO Mindstorms EV3 robot using Python scripts. The project consists of two main parts: a main control script (`main.py`) and a communication script (`ev3_comm.py`).

## Prerequisites

- LEGO Mindstorms EV3 kit
- Pybricks MicroPython firmware
- Basic knowledge of Python programming

## Project Structure

- `main.py`: This script controls the EV3 robot's movements based on readings from two ultrasonic sensors.
- `ev3_comm.py`: This script sets up a server for communication between the EV3 and a PC.

## Installation

1. Install the Pybricks MicroPython firmware on your EV3 brick. Follow the instructions on the [Pybricks website](https://pybricks.com/ev3-micropython).

2. Upload the `main.py` and `ev3_comm.py` scripts to your EV3 brick.

## Usage

### Running the Main Control Script

The `main.py` script controls the EV3 robot's movements based on ultrasonic sensor readings. It operates in a loop, continuously checking the distances from the sensors and moving a motor accordingly.

To run the script:

1. Make sure the EV3 brick is turned on and the sensors and motor are connected to the correct ports.
2. Execute the script on the EV3 brick.

### Running the Communication Script

The `ev3_comm.py` script sets up a TCP server on the EV3 brick for communication with a PC. It sends and receives messages in a loop.

To run the script:

1. Make sure the EV3 brick is connected to the same network as the PC.
2. Execute the script on the EV3 brick.

### Manual Mode

By default, the `main.py` script runs in manual mode (`manuel = True`). In this mode, the EV3 robot uses the ultrasonic sensors to move a platform up and down based on the distance readings.

### Autonomous Mode

To switch to autonomous mode, set `manuel = False` in the `main.py` script. This mode is reserved for future AI code implementation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Grayson Talbot for most of the codebase.
- GPT-4o for the networking script.
- Visual Studio Code (VSCode), Socket, Python, and GitHub for their libraries and hosting.
- Creative Mindstorms for email help.
- LEGO Mindstorms EV3 for the hardware.
- Rasberry Pi for the main ai hardware.
- Google for the tpu and ai dataset.
- Pybricks MicroPython for the Mindstorm libraries.
