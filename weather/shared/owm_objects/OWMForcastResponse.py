from . import OWMForcastSingleDay as OFSD


class OWMForcastResponse:

    def __init__(self, json_data):
        singleDayList = json_data["list"]
        self.dayList = []
        for i in range(0, len(singleDayList)):
            self.dayList.append(OFSD.OWMForcastSingleDay(singleDayList[i]))

    def getDayList(self):
        return self.dayList
