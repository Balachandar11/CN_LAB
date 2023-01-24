import socket
HOST = 'localhost'
port = 1234
table ={
'1E.4A.4A.11':'192.168.1.1',
'5E.51.4B.01':'192.168.2.1',
'4B.35.CD.32':'192.168.1.3',
'AF.4D.1F.FF':'192.168.4.1',
'C3.C5.EE.C2':'192.168.3.2'
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
    mac = clientsocket. recv( 1024)
    mac =mac.decode('utf-8')
    if mac == 'exit':
        print("Server Exiting")
        break
    ip = table.get(mac,'No entry for given mac address')
    clientsocket.send(ip.encode())

s.close()