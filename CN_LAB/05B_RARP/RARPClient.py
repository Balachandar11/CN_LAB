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
    add = input('Enter MAC :')
    if add =='exit':
        s.send(add.encode())
        time.sleep(2)
        print("Exiting")
        break
    s.send(add.encode())
    ip = s.recv( 1024)
    ip = ip.decode("utf-8")
    print('IP of',add,' is : ',ip)
s.shutdown(2)
s.close()
