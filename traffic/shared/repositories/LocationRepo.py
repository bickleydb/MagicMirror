import traffic.models.LocationModel as LM

class LocationRepo:

    def GetAllLocations(self):
        LocationManager = LM.LocationModel.get_manager()
        return LocationManager.all()

    def GetLocationByUniqueID(self, unique_id):
        LocationManager = LM.LocationModel.get_manager()
        return LocationManager.get(uniqueId=unique_id)

    def GetStartingPos(self):
        return self.GetAllLocations()[0]

    def GetEndingPos(self):
        return self.GetAllLocations()[1]

