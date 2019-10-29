import socket
import select
import sys
#from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_ADDRESS = str(sys.argv[1])
PORT = int(sys.argv[2])

server.bind((IP_ADDRESS, PORT))

server.listen(100)

client_list = []

def clientThread(conn, addr):
    conn.send("Welcome to the room!")

    while True:
        try:
            message = conn.recv(2048)
            if message:
                message_to_send =  "<" + addr[0] + "> " + message
                print(message_to_send)

                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue    

def broadcast(message, connection):
    for client in client_list:
        if client!=connection: 
            try:
                client.send(message)
  
                # if the link is broken, we remove the client 
                remove(client)
            except:
                continue

def remove(connection):
    if connection in client_list:
        list_of_clients.remove(connection)

while True:
  
    """Accepts a connection request and stores two parameters,  
    conn which is a socket object for that user, and addr  
    which contains the IP address of the client that just  
    connected"""
    conn, addr = server.accept() 
  
    """Maintains a list of clients for ease of broadcasting 
    a message to all available people in the chatroom"""
    list_of_clients.append(conn) 
  
    print(addr[0] + " connected")

    start_new_thread(clientthread,(conn,addr))     
  
conn.close() 
server.close() 