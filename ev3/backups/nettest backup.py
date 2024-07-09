#!/usr/bin/env pybricks-micropython
import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 54321))  # Bind to all interfaces on port 54321
server_socket.listen(1)

print("Waiting for connection...")
client_socket, client_address = server_socket.accept()
print("Accepted connection from:", client_address)

try:
    # Example variable to send
    variable_to_send = "Hello from EV3"
    data = variable_to_send.encode()

    # Send the data to the PC
    total_sent = 0
    while total_sent < len(data):
        sent = client_socket.send(data[total_sent:])
        if sent == 0:
            raise RuntimeError("Socket connection broken")
        total_sent += sent

    # Receive data from the PC
    received_data = client_socket.recv(1024).decode('utf-8')
    print("Received from PC:", received_data)

finally:
    # Ensure the connection is closed properly
    client_socket.close()
    server_socket.close()

print("Communication ended")
