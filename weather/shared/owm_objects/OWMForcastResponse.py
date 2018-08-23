from . import OWMForcastSingleDay

class OWMForcastResponse:

    def __init__(self,json_data):
        singleDayList = json_data["list"]
        self.dayList = []
        for i in range(0,len(singleDayList)):
            self.dayList.append(OWMForcastSingleDay.OWMForcastSingleDay(singleDayList[i]))

    def getDayList(self):
        return self.dayList