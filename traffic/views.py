from django.shortcuts import render
from django.http import HttpResponse
from .queries.GoogleMapsRouteQuery import GoogleMapsRouteQuery
from .shared.LocationRepo import LocationRepo

from . import GOOGLE_API_KEY

def index(request):

    baseRepo = LocationRepo()
    query = GoogleMapsRouteQuery(Starting_Location=baseRepo.GetStartingPos(), Ending_Location=baseRepo.GetEndingPos(), Api_Key=GOOGLE_API_KEY)
    return HttpResponse(query.getResult())

# Create your views here.
