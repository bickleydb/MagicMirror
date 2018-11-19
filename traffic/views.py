from django.shortcuts import render
from django.http import HttpResponse
from .queries.GoogleMapsRouteQuery import GoogleMapsRouteQuery
from .shared.repositories.LocationRepo import LocationRepo
from .shared.repositories.PathRepo import PathRepo
from .shared.repositories.PathEstimationRepo import PathEstimationRepo

from . import GOOGLE_API_KEY

def index(request):
    baseRepo = LocationRepo()
    query = GoogleMapsRouteQuery(Starting_Location=baseRepo.GetStartingPos(), Ending_Location=baseRepo.GetEndingPos(), Api_Key=GOOGLE_API_KEY)
    return HttpResponse(query.getResult())

def GetPath(request):

    startingLocation = request.GET["startingLocation"]
    endingLocation = request.GET["endingLocation"]
    pathRepo = PathRepo()
    baseRepo = LocationRepo()
    pathInstance = pathRepo.GetPathBetween(baseRepo.GetLocationByUniqueID(startingLocation),baseRepo.GetLocationByUniqueID(endingLocation))
    return HttpResponse(pathInstance)

def GetPathEstimate(request):
    pathRepo = PathRepo()
    baseRepo = LocationRepo()
    estimateRepo = PathEstimationRepo()
    pathInstance = pathRepo.GetPathBetween(baseRepo.GetStartingPos(),baseRepo.GetEndingPos())
    return HttpResponse(estimateRepo.GetEstimationForPath(pathInstance))

def RecordPathEstimate(request):
    pathRepo = PathRepo()
    baseRepo = LocationRepo()
    estimateRepo = PathEstimationRepo()

    pathInstance = pathRepo.GetPathBetween(baseRepo.GetStartingPos(),baseRepo.GetEndingPos())
    return HttpResponse(estimateRepo.RecordNewEstimationForPath(pathInstance))


def RecalculatePathEstimate(request):
    pathRepo = PathRepo()
    baseRepo = LocationRepo()
    estimateRepo = PathEstimationRepo()

    pathInstance = pathRepo.GetPathBetween(baseRepo.GetStartingPos(),baseRepo.GetEndingPos())
    return HttpResponse(estimateRepo.RecalculateEstimateForPath(pathInstance))
# Create your views here.
