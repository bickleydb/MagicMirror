import json


class AppListResponse:

    def __init__(self, appList, appConfigDict):
        self.appList = appList
        self.appConfigDict = appConfigDict

    def to_json(self):
        return self.app_list_to_json(self.appList, self.appConfigDict)

    def app_list_to_json(self, appList, appConfigDict):
        jsonStr = "["
        for app in appList:
            if app.name in appConfigDict:
                jsonStr = self.add_app_config(app, jsonStr, appConfigDict)
        jsonStr = jsonStr[:-1]
        jsonStr = jsonStr + "]"
        return jsonStr

    def add_app_config(self, app, baseStr, appConfigDict):
        baseStr += self.app_config_to_json(app, appConfigDict[app.name])
        baseStr += ","
        return baseStr

    def app_config_to_json(self, app, appConfig):
        return json.dumps({
            "name": app.name,
            "bundlePath": app.bundlePath,
            "StartRow": appConfig.startRow,
            "EndRow": appConfig.endRow,
            "StartColumn": appConfig.startColumn,
            "EndColumn": appConfig.endColumn,
            "Priority": appConfig.startOnStartup
         })
