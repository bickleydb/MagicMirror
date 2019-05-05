import requests
import json

class GoogleCalendarQuery:

    def __init__(self, calendarId):
        self.calendarId = calendarId