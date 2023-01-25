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
s.connect((hname,port))

s.send(b"GET / HTTP/1.1\r\nHost:%b\r\n\r\n"%(hname.encode()))
print(s.recv(4096).decode())