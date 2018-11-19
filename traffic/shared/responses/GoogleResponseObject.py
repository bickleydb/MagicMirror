import json

from . import TrafficResponseObject
class GoogleResponseObject(TrafficResponseObject.TrafficResponse):

    json_data = ""

    duration = 0
    distance = 0

    def __init__(self, json_data=""):
        print(json_data)
        self.json_data = json_data
       
        parsedData = json.loads(json_data)
        
        self.distance = self.parseDistance(parsedData)
        self.duration = self.parseDuration(parsedData)

    def getDistance(self):
        return self.distance
    
    def getDuration(self):
        return self.duration

    def parseDistance(self, parsedData):
        return parsedData["routes"][0]["legs"][0]["distance"]
    
    def parseDuration(self, parsedData):
        return parsedData["routes"][0]["legs"][0]["duration"]