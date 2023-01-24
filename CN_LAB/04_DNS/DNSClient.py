import socket

# DNS server to query
DNS_SERVER = "localhost"

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket connected successfully")
print("Type exit to exit")
while(True):
    # Prompt the user for a host name
    hostname = input("Enter a host name: ")
    if hostname == 'exit':
        sock.sendto(hostname.encode(), (DNS_SERVER, 5055))
        print("exiting")
        break
    # Send a DNS query for the host name to the server
    query = hostname.encode()
    sock.sendto(query, (DNS_SERVER, 5055))

    # Receive the response
    response, addr = sock.recvfrom(1024)

    # Print the response
    print('the ip address of %s is %s' %(hostname,response.decode()))
sock.shutdown(1)
sock.close()
