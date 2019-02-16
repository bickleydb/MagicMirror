from django.shortcuts import render
from django.http import HttpResponse
import json
from traffic.shared.repositories import CalendarRepo
import httplib2
# from oauth2client.contrib import gce


def __getCalendarByName(name):
    calendarRepo = CalendarRepo.GoogleCalendarRepo()
    return calendarRepo.GetCalendarByID(id)


def getCalendarById(request):
    name = request.GET["name"]
    instance = __getCalendarByName(name)
    return HttpResponse(instance.calendar_name)


def getEventsInCalendar(request):
    name = request.GET["name"]
    # credentials = gce.AppAssertionCredentials(
    #   scope='https://www.googleapis.com/auth/calendar.events.readonly'
    # )
    # http = credentials.authorize(httplib2.Http())
