import requests
import json

from . import RouteQuery

class GoogleMapsRouteQuery (RouteQuery.RouteQuery):
        
    base_url = 'https://maps.googleapis.com/maps/api/directions/json?origin={startingPoint}&destination={endingPoint}&key={apiKey}'
    Starting_Location = None
    Api_Key = ""
    Ending_Location = None



    def __init__(self, Starting_Location=None, Ending_Location=None, Api_Key=""):
        self.Starting_Location = Starting_Location
        self.Ending_Location = Ending_Location
        self.Api_Key = Api_Key

    def getApiKey(self):
        return self.Api_Key

    def getStartingPoint(self):
        return self.Starting_Location

    def getEndingPoint(self):
        return self.Ending_Location

    def getBaseURL(self):
        return self.base_url

    def formatAddress(self, location):
        return location.address.replace(" ","+") + "+" + location.city.replace(" ","+") + "+" + location.postalCode.replace(" ","+")

    def getURL(self):
        return self.getBaseURL().format(
            startingPoint=self.formatAddress(self.getStartingPoint()),
            endingPoint=self.formatAddress(self.getEndingPoint()),
            apiKey=self.getApiKey(),
        )

    def getResult(self):
        url = self.getURL()
        response = requests.get(url)
        return response