import traffic.models.LocationModel as LM

class LocationRepo:

    def GetAllLocations(self):
        LocationManager = LM.LocationModel.get_manager()
        return LocationManager.all()

    def GetStartingPos(self):
        return self.GetAllLocations()[0]

    def GetEndingPos(self):
        return self.GetAllLocations()[1]

