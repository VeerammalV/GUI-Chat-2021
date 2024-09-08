import socket

PORT 50000

HOST=socket.gethostbyname (socket gethostname())

ADDRESS=(HOST, PORT)

FORMAT="utf-8"

clients=[]

names=[]

#Create a new socket for server where AF_INET is the type of address (will return IPv4) and Sock_STREAM is the TCP socket

server = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
 
 def startchat():
 	print("server is working on"+HOST)
 
    server.listen()
    
    while True:
    	connection, addr = server.accept()
    	connection.send("Name".encode(FORMAT))
        
        name = connection.recv(1025).decode(FORMAT)
        
        names.append(name)
        
       clients.append(connection)
       
          print(f"Name is: {name}")
          #print(f"Client is: {connection}")
           
       
          broadcastMessage(f"{name} has joined the group".encode(FORMAT))
          
          connection.send("Connection successful".encode (FORMAT))

thread threading. Thread(target=receive, args=(connection, addr))

thread.start()

print(f"active connections {threading.active_count()-1}")

def receive (connection, addr):

print("New Connection {addr}")

connected =True

while connected:

message = connection.recv(1025)

broadcastMessage (message)

connection.close()

def broadcastMessage (message):

for client in clients:
	client.send(message)
	