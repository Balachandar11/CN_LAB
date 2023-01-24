import socket,time
Host = 'localhost'
Port = 1234
try:
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Socket Creation Error %s"%(err))
s.connect((Host, Port))
print("Succesfully connected with server")
print("Enter exit to EXIT")

while(True):
    add = input('Enter IP :')
    if add =='exit':
        s.send(add.encode())
        time.sleep(2)
        print("Exiting")
        break
    s.send(add.encode())
    mac = s.recv( 1024)
    mac = mac.decode("utf-8")
    print('MAC of',add,' is : ',mac)
s.shutdown(2)
s.close()
