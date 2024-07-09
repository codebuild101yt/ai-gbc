# EV3 Mindstorms Project

This project involves controlling a LEGO Mindstorms EV3 robot using Python scripts. The project consists of three main parts: a main control script (`main.py`), a communication script for the EV3 (`ev3_comm.py`), and a communication script for the PC.

## Prerequisites

- LEGO Mindstorms EV3 kit
- Pybricks MicroPython firmware
- Basic knowledge of Python programming

## Project Structure

- `main.py`: This script controls the EV3 robot's movements based on readings from two ultrasonic sensors.
- `ev3_comm.py`: This script sets up a server for communication between the EV3 and a PC.
- `pc.py`: This script runs on the PC to communicate with the EV3 over a network.

## Installation

1. Install the Pybricks MicroPython firmware on your EV3 brick. Follow the instructions on the [Pybricks website](https://pybricks.com/ev3-micropython).

2. Upload the `main.py` and `ev3_comm.py` scripts to your EV3 brick.

3. Save the `pc.py` script to your PC.

## Usage

### Running the Main Control Script

The `main.py` script controls the EV3 robot's movements based on ultrasonic sensor readings. It operates in a loop, continuously checking the distances from the sensors and moving a motor accordingly.

To run the script:

1. Make sure the EV3 brick is turned on and the sensors and motor are connected to the correct ports.
2. Execute the script on the EV3 brick.

### Running the Communication Script on EV3

The `ev3_comm.py` script sets up a TCP server on the EV3 brick for communication with a PC. It sends and receives data used for the ai.

To run the script:

1. Make sure the EV3 brick is connected to the same network as the PC(i used the included usb cable to act like a ethernet cable but your solotion can be defrent).
2. Execute the script on the EV3 brick.

### Running the Communication Script on PC

The `pc_client.py` script runs on the PC and connects to the EV3 to communicate over the network.

To run the script:

1. Ensure the PC is on the same network as the EV3.
2. Replace the `ev3_ip` variable with the EV3's IP address in the `pc.py` script.
3. Execute the script on the PC.

### Manual Mode

By default, the `main.py` script runs in manual mode (`manuel = True`). In this mode, the EV3 robot uses the ultrasonic sensors to move a platform up and down based on the distance readings.

### Autonomous Mode

To switch to autonomous mode, set `manuel = False` in the `main.py` script. This mode is reserved for future AI code implementation.

## Code

### PC Client Script (`pc_client.py`)

```python
import socket
import time

def start_client():
    ev3_ip = "10.93.168.34"  # Replace with your EV3's IP address
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ev3_ip, port))

    print("Connected to EV3")

    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                print("Received from EV3:", data)
            
            variable_to_send_back = int(data) + 1
            client_socket.sendall(str(variable_to_send_back).encode())

            time.sleep(1)

    finally:
        client_socket.close()

if __name__ == "__main__":
    print("Starting client...")
    start_client()
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

### Grayson Talbot
- Contributed most of the codebase.
- GitHub: [codebuild101yt](https://github.com/codebuild101yt)

### GPT-4
- Developed the networking script.
- Organization: [OpenAI](https://www.openai.com/)

### Creative Mindstorms
- Provided email support.
- GitHub: [CreativeMindstorms](https://github.com/CreativeMindstorms)

### Tools and Resources
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/): For the development environment.
- [Socket Library](https://docs.python.org/3/library/socket.html): For networking communication.
- [Python](https://www.python.org/): The programming language used for scripting.
- [GitHub](https://github.com/): For code hosting and version control.
- [LEGO Mindstorms EV3](https://www.lego.com/mindstorms): For the robotics kit.
- [Pybricks MicroPython](https://pybricks.com/ev3-micropython): For the firmware used on the EV3 brick.


