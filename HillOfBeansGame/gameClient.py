'''
Created on Jul 30, 2017

@author: metha
'''
import socket
import json
from training.data import gameData

total = 0
HOST, PORT = "localhost", 8888
testData = "{\"currentBeans\": 1, \"maxToTake\": 3, \"totalStarting\": 4}"
dataSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dataSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
maxToTake = 3
totalStarting = 0

def initSocket():
        global dataSocket
        dataSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dataSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        dataSocket.connect((HOST, PORT))

def otherTurn(totalLeft):
    global dataSocket
    initSocket();
    print("Current total: %i" % total)
    sendPackage = gameData.GameRequest(totalLeft, maxToTake, totalStarting)
    dataSocket.sendall(str.encode(sendPackage.encodeJSON()))
    recvData = json.loads(str(dataSocket.recv(1024), "utf-8"))
    response = gameData.GameResponse(recvData['numToTake'], recvData['totalLeft'])
    dataSocket.close()
    
    return response.numToTake

def playTheGame():
    total = int(input("Enter total number of beans:\n"))
    totalStarting = total
    print("There are ", total, "beans left.")
    
    while True:
        numToTake = int(input("How many do you want to take?\n"))
        
        if (numToTake > total) or (numToTake > maxToTake):
            print("You can't take that many.\n")
        elif numToTake <= 0:
            print ("You must take at least one bean.\n")
        else:
            total -= numToTake
            if total == 0:
                print("\nYou have won!")
                break
            else:
                print("There are ", total, " beans left.")
                total -= otherTurn(total)
                print("Player 2 made the total ", total)
                if total == 0:
                    print("\nThe other player has won.");
                    break
                else:
                    print("There are ", total, "beans left.\n")    

if __name__ == '__main__':
    playTheGame()
