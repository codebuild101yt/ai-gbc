import socket
import time
from Counter import get_output  # Import the function

def start_client():
    ev3_ip = "localhost"  # Replace with your EV3's IP address
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ev3_ip, port))

    print("Connected to EV3")
    last_variable_to_send_back = None
    try:
        while True:
            new_value = get_output()  # Call the function to get the output value

            if new_value is not None:
                last_variable_to_send_back = int(new_value)

            if last_variable_to_send_back is not None:
                variable_to_send_back = last_variable_to_send_back
            else:
                print("No previous value found. Please enter a new value.")
                continue

            client_socket.sendall(str(variable_to_send_back).encode())
            time.sleep(1)

    finally:
        client_socket.close()

if __name__ == "__main__":
    print("Starting client...")
    start_client()

