from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader 
from datetime import datetime
import json
# Create your views here.

def getTime(request):
    return JsonResponse(getCurrentTimeDictionary())
    

def getCurrentTimeDictionary():
    currentTime = datetime.now()
    currentHour = currentTime.strftime("%I")
    currentMinute = currentTime.strftime("%M")
    return {
        "hourFirstDigit" : currentHour[0],
        "hourSecondDigit" : currentHour[1],
        "hourSeperator" : ":",
        "minuteFirstDigit" : currentMinute[0],
        "minuteSecondDigit" : currentMinute[1],
        "dayOfWeek" : currentTime.strftime("%A"),
        "dayOfWeekSeperator" : ", ",
        "month" : currentTime.strftime("%B"),
        "dayOfMonth" : currentTime.strftime("%d"),
        "year" : currentTime.strftime("%Y")
    }


def index(request):
    template = loader.get_template('timeapp/small.html')
    return HttpResponse(template.render(getCurrentTimeDictionary(),request))