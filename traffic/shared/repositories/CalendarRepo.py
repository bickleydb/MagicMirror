import traffic.models.Calendar.Google.GoogleCalendarModel as GCM


class GoogleCalendarRepo:

    def GetCalendarByID(self, id):
        repo = GCM.GoogleCalendarModel.get_manager()
        return repo.get(calendar_id=id)

    def GetCalendarByName(self, name):
        repo = GCM.GoogleCalendarModel.get_manager()
        return repo.get(calendar_name=id)
