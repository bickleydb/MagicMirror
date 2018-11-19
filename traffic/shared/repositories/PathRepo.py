from traffic.models.Path import Path

class PathRepo:

    def GetPathBetween(self, startingPoint, endingPoint):
        PathManager = Path.get_manager()
        return PathManager.all().filter(StartingLocation=startingPoint, EndingLocation=endingPoint)[0]
