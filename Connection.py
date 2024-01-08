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
server_socket.listen(2)
print(f"Server listening on {host}:{port}")

# Accept a connection
client_socket1, client_address1 = server_socket.accept()
print(f"Connection from {client_address1}")
print(f"Server listening on {host}:{port}")

# Accept a connection
client_socket2, client_address2 = server_socket.accept()
print(f"Connection from {client_address2}")
while True:
    # Receive a response from the client
    data1 = client_socket1.recv(1024)
    if not data1:
        break
    data2 = client_socket2.recv(1024)
    if not data2:
        break
    print(f"Received from client: {data1.decode()}")
    print(f"Received from client: {data2.decode()}")

    # Send a response back to the client
    # str(dir) + ":" + str(time)
    
    response = input("Bot No:enter dir:time") #10
    client_socket1.sendall(response.encode())
    client_socket2.sendall(response.encode())
# Close the connection
client_socket1.close()
client_socket2.close()
server_socket.close()