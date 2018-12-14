from traffic.models.PathEstimationModel import PathEstimationModel
from traffic.models.PathLengthModel import PathLengthModel
from traffic.queries.GoogleMapsRouteQuery import GoogleMapsRouteQuery
from traffic.shared.responses.GoogleResponseObject import GoogleResponseObject
from django.db.models import Avg
from traffic import GOOGLE_API_KEY


class PathEstimationRepo:

    def GetEstimationForPath(self, pathInstance):
        EstimatedInstances = PathEstimationModel.get_manager()
        return EstimatedInstances.all().filter(pathInstance=pathInstance)[0]

    def RecordNewEstimationForPath(self, path):
        res = GoogleMapsRouteQuery(Starting_Location=path.StartingLocation,
                                   Ending_Location=path.EndingLocation,
                                   Api_Key=GOOGLE_API_KEY).getResult()

        pathLengthManager = PathLengthModel.get_manager()
        pathLengthManager.create(
            pathInstance=path,
            secondsPerTrip=res.getDuration()["value"]
        )

    def RecalculateEstimateForPath(self, pathInstance):
        pathLengthManager = PathLengthModel.get_manager()
        avgVal = pathLengthManager.all().filter(
            pathInstance=pathInstance
            ).aggregate(value=Avg('secondsPerTrip'))
        return avgVal
