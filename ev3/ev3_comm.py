#!/usr/bin/env pybricks-micropython
#!/usr/bin/env pybricks-micropython
import socket
import utime

class EV3Server:
    def __init__(self, port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', port))  # Bind to all interfaces on the given port
        self.server_socket.listen(1)
        self.client_socket = None

    def wait_for_connection(self):
        print("Waiting for connection...")
        self.client_socket, client_address = self.server_socket.accept()
        print("Accepted connection from:", client_address)

    def send_message(self, message):
        data = str(message).encode()
        total_sent = 0
        while total_sent < len(data):
            sent = self.client_socket.send(data[total_sent:])
            if sent == 0:
                raise RuntimeError("Socket connection broken")
            total_sent += sent

    def receive_message(self):
        data = self.client_socket.recv(1024).decode('utf-8')
        if data:
            return data
        return None

    def close_connection(self):
        if self.client_socket:
            self.client_socket.close()
        self.server_socket.close()

# This part will only execute if the script is run directly, not if it's imported
if __name__ == "__main__":
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
