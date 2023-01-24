import socket
import sys
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Succesfully created")
except socket.error as err:
    print("Socket creation failed with error %s" %(err))
port = 80

hname = input("Enter host address(www.examgle.com):")
try:
    host_ip = socket.gethostbyname(hname)
except socket.gaierror:
 
    # this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()

s.connect((host_ip,port))

s.sendall(b"GET/HTTP/1.0\r\nHost:www.youtube.com\r\nAccept:text/html\r\n\r\n")
print(str(s.recv(4096),'utf-8'))