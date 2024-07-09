# `ev3_comm.py` Documentation

## Overview

`ev3_comm.py` is a module designed to facilitate TCP/IP communication between an EV3 robot and a PC. It encapsulates the server functionality in a class that can be imported and used in other scripts.

## Class: `EV3Server`

### Methods

#### `__init__(self, port=12345)`

- **Description**: Initializes the server socket and binds it to the specified port.
- **Parameters**:
  - `port` (int): The port number to bind the server to. Default is `12345`.

#### `wait_for_connection(self)`

- **Description**: Waits for a client to connect to the server.
- **Returns**: None.

#### `send_message(self, message)`

- **Description**: Sends a message to the connected client.
- **Parameters**:
  - `message` (str/int): The message to send. It will be converted to a string and encoded to bytes.
- **Returns**: None.

#### `receive_message(self)`

- **Description**: Receives a message from the connected client.
- **Returns**:
  - `str`: The message received from the client. Returns `None` if no data is received.

#### `close_connection(self)`

- **Description**: Closes the connection with the client and the server socket.
- **Returns**: None.

## Usage Example

```python
from ev3_comm import EV3Server
import utime

server = EV3Server()
server.wait_for_connection()

try:
    variable_to_send = 0
    while True:
        server.send_message(variable_to_send)
        variable_to_send += 1
        utime.sleep(1)
        received_data = server.receive_message()
        if received_data:
            print("Received from PC:", received_data)
finally:
    server.close_connection()
    print("Communication ended")
