import socket


host = '127.0.0.1'
port = 5252

mainSock = socket.socket()
mainSock.connect((host,port))

message = 'Hello from client (Bob)'
mainSock.send(message.encode())

data = mainSock.recv(1024).decode()

print('Received from server : ' + data)


mainSock.close()