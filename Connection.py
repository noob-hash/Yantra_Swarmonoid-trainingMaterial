import socket
import time

import socket

# Set the IP address and port on which the laptop server will listen
host = '0.0.0.0'  # Listen on all available interfaces
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {host}:{port}")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:
    # Receive a response from the client
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received from client: {data.decode()}")

    # Send a response back to the client
    # str(dir) + ":" + str(time)
    
    response = input("enter dir:time")
    client_socket.sendall(response.encode())
# Close the connection
client_socket.close()
server_socket.close()

