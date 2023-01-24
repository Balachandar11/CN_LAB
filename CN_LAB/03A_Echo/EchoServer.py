
import socket

HOST = 'localhost'   
#use any port >1023 
PORT = 5005  
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Succesfully created")
except socket.error as err:
    print("Socket creation failed with error %s" %(err))

s.bind((HOST, PORT))
# 1 means the number of accepted connections
s.listen(1)  
# waits for a new connection
conn, addr = s.accept()  
print('Client connected: ', addr)
while True:
    data = conn.recv(1024)
    
    if not data:
        break
    print('Data recieved from client : %s '%(data.decode()))    
    conn.sendall(data)
conn.close()