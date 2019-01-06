from django.shortcuts import render
from django.http import HttpResponse
from traffic.queries.GoogleMapsRouteQuery import GoogleMapsRouteQuery
from traffic.shared.repositories.LocationRepo import LocationRepo
from traffic.shared.repositories.PathRepo import PathRepo
from traffic.shared.repositories.PathEstimationRepo import PathEstimationRepo


def index(request):
    baseRepo = LocationRepo()
    query = GoogleMapsRouteQuery(Starting_Location=baseRepo.GetStartingPos(),
                                 Ending_Location=baseRepo.GetEndingPos(),
                                 Api_Key=GOOGLE_API_KEY)
    return HttpResponse(query.getResult())


def GetPath(request):
    startingLocation = request.GET["startingLocation"]
    endingLocation = request.GET["endingLocation"]
    pathRepo = PathRepo()
    baseRepo = LocationRepo()
    pathInstance = pathRepo.GetPathBetween(
        baseRepo.GetLocationByUniqueID(startingLocation),
        baseRepo.GetLocationByUniqueID(endingLocation))
    return HttpResponse(pathInstance)


def GetPathEstimate(request):
    pathRepo = PathRepo()
    baseRepo = LocationRepo()
    estimateRepo = PathEstimationRepo()
    pathInstance = pathRepo.GetPathBetween(
        baseRepo.GetStartingPos(),
        baseRepo.GetEndingPos()
    )
    return HttpResponse(estimateRepo.GetEstimationForPath(pathInstance))


def RecordPathEstimate(request):
    pathRepo = PathRepo()
    baseRepo = LocationRepo()
    estimateRepo = PathEstimationRepo()

    pathInstance = pathRepo.GetPathBetween(
        baseRepo.GetStartingPos(),
        baseRepo.GetEndingPos()
    )
    return HttpResponse(estimateRepo.RecordNewEstimationForPath(pathInstance))


def RecalculatePathEstimate(request):
    pathRepo = PathRepo()
    baseRepo = LocationRepo()
    estimateRepo = PathEstimationRepo()

    pathInstance = pathRepo.GetPathBetween(
        baseRepo.GetStartingPos(),
        baseRepo.GetEndingPos()
    )
    return HttpResponse(estimateRepo.RecalculateEstimateForPath(pathInstance))
