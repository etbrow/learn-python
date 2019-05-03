'''
Created on Jul 29, 2017

@author: metha
'''
import socketserver
import socket
import json
from training.data import gameData

HOST, PORT = '', 8888

class TCPHandler(socketserver.BaseRequestHandler):
	def handle(self):
		print("Got data")
		self.data = self.request.recv(1024).strip()
		print("data")
		print(self.data)
		parseData = json.loads(self.data)
		gamePackage = gameData.GameRequest(parseData['currentBeans'], parseData['maxToTake'], parseData['totalStarting'])
		
		self.request.sendall(str.encode(takeTurn(gamePackage).encodeJSON() + "\n"))
		print("Sent %s" % str.encode(takeTurn(gamePackage).encodeJSON()))
		
def takeTurn(gamePackage):
		numToTake = gamePackage.currentBeans%(gamePackage.maxToTake) + 1
		print("There are %i beans and I can take no more than %i so I'm taking %i" % (gamePackage.currentBeans, gamePackage.maxToTake, numToTake))
		totalLeft = gamePackage.currentBeans - numToTake
		
		response = gameData.GameResponse(numToTake, totalLeft)
		return response
	
if __name__ == '__main__':
	server = socketserver.TCPServer((HOST, PORT), TCPHandler)
	server.allow_reuse_address = True
	server.socket_type = socketserver.socket.SOCK_STREAM
	
	print("starting server")
	server.serve_forever()
