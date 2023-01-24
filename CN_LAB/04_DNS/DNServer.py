import socket

# IP and port to bind the server to
IP = "localhost"
PORT = 5055

# Create a dictionary to store host names and IP addresses
hosts = {"www.google.com": "192.168.1.100", "www.yahoo.com": "192.168.1.101",'www.bing.com':'192.168.1.102'}

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server is running")
# Bind the socket to the IP and port
server_socket.bind((IP, PORT))


# Handle incoming queries
while True:
    # Receive a query
    query, addr = server_socket.recvfrom(1024)

    # Extract the host name from the query
    hostname = query.decode()

    # Look up the host name in the dictionary
    if hostname in hosts:
        # Send the IP address as the response
        ip = hosts[hostname]
        response = ip.encode()
        server_socket.sendto(response, addr)
    else:
        # Send an error message if the host name is not found
        response = b"Error: Host not found"
        server_socket.sendto(response, addr)
