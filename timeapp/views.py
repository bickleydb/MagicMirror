from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from datetime import datetime, timedelta
import json

global startTime
startTime = datetime.now()


def getTime(request):
    startTime = startTime + timedelta(days=1)
    return JsonResponse(getCurrentTimeDictionary(startTime))


def getCurrentTimeDictionary(currentTime):
    currentHour = currentTime.strftime("%I")
    currentMinute = currentTime.strftime("%M")
    return {
        "hourFirstDigit": currentHour[0],
        "hourSecondDigit": currentHour[1],
        "hourSeperator": ":",
        "hourFirstDigitPercent": int(currentHour[0])*10,
        "hourSecondDigitPercent": int(currentHour[1])*10,
        "minuteFirstDigit": currentMinute[0],
        "minuteSecondDigit": currentMinute[1],
        "minuteFirstDigitPercent": int(currentMinute[0])*10,
        "minuteSecondDigitPercent": int(currentMinute[1])*10,
        "dayOfWeek": currentTime.strftime("%A"),
        "dayOfWeekSeperator": ", ",
        "month": currentTime.strftime("%B"),
        "dayOfMonth": currentTime.strftime("%d"),
        "year": currentTime.strftime("%Y")
    }


def index(request):
    template = loader.get_template('timeapp/small.html')
    return HttpResponse(template.render(getCurrentTimeDictionary(startTime), request))
