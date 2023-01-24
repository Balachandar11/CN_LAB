import socket
HOST = 'localhost'
port = 1234
table ={
'192.168.1.1':'1E.4A.4A.11',
'192.168.2.1':'5E.51.4B.01',
'192.168.1.3':'4B.35.CD.32',
'192.168.4.1':'AF.4D.1F.FF',
'192.168.3.2':'C3.C5.EE.C2',
}
try:
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Socket Creation Error %s"%(err))
s.bind((HOST,port))
s.listen()
clientsocket,address = s.accept()
print("Connection From address",address, " Has Established")
while(True):
    ip = clientsocket. recv( 1024)
    ip =ip.decode('utf-8')
    if ip == 'exit':
        print("Server Exiting")
        break
    mac = table.get(ip,'No entry for given address')
    clientsocket.send(mac.encode())

s.close()