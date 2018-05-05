import json

class AppListResponse:

    def __init__(self, appList, appConfigDict):
        self.appList = appList
        self.appConfigDict = appConfigDict

    def toJSON(self):
        return self.AppListToJSON(self.appList, self.appConfigDict)

    def AppListToJSON(self, appList, appConfigDict):
        jsonStr = "["
        for app in appList:
            if app.name in appConfigDict:
                jsonStr = jsonStr + self.AppConfigToJSON(app, appConfigDict[app.name])
                jsonStr = jsonStr + ","
        jsonStr = jsonStr[:-1]
        jsonStr = jsonStr + "]"
        return jsonStr
        
    def AppConfigToJSON(self, app, appConfig):
        return json.dumps({
            "name"        : app.name,
            "bundlePath"  : app.bundlePath,
            "StartRow"    : appConfig.startRow,
            "EndRow"      : appConfig.endRow,
            "StartColumn" : appConfig.startColumn,
            "EndColumn"   : appConfig.endColumn,   
            "Priority"    : appConfig.startOnStartup     
         })