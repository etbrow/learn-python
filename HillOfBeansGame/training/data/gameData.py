'''
Created on Jul 29, 2017

@author: metha
'''
import json

class GameRequest(object):
    '''
    classdocs
    '''
    def encodeJSON(self):
        return json.dumps(self.__dict__)

    def __init__(self, currentBeans, maxToTake, totalStarting):
        self.currentBeans = currentBeans
        self.maxToTake = maxToTake
        self.totalStarting = totalStarting
        
class GameResponse(object):
    def encodeJSON(self):
        return json.dumps(self.__dict__)
    
    def decodeJSON(self, data):
        decoded = json.loads(data)
        self.numToTake = decoded['numToTake']
        self.totalLeft = decoded['totalLeft']
    
    def __init__(self, numToTake, totalLeft):
        self.numToTake = numToTake
        self.totalLeft = totalLeft