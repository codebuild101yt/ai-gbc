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
