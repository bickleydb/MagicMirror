from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import os
import pdb

from home.shared.repositories import AppRepo, CSSRepo, FontRepo, UIConfigRepo, MagicMirrorConfigRepo

def loadHTML(request):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render({
        "fontList" :FontRepo.FontRepo().loadFonts()
    }))


def loadAppConfig(request):
    appRepo = MagicMirrorConfigRepo.MagicMirrorConfigRepo()
    return HttpResponse(translateConfigToJson(appRepo.loadConfiguration()))


def loadApplications(request):
    appRepo = AppRepo.AppRepo()
    uiInfo = UIConfigRepo.UIConfigRepo()
 
    appList = appRepo.get_application_list()

    uiConfigValues = {}

    for app in appList:
        uiConfigList = uiInfo.get_ui_for_app(app)
        if len(uiConfigList) != 0:
            uiConfigValues[app.name] = uiInfo.get_ui_for_app(app)[0].UI_Config
 
    response = HttpResponse(translateAppListToJson(appList, uiConfigValues))
    return response

def translateConfigToJson(config):
    return json.dumps({
        "rows" : config.rows,
        "columns" : config.columns,
        "widthValue" : config.width_value, 
        "widthUnit" : config.width_unit,
        "heightValue": config.height_value,
        "heightUnit" : config.height_unit,      
    })

def translateAppListToJson(appList, configValues):
    jsonStr = "["
    for value in appList:
        if value.name in configValues:
            jsonStr = jsonStr + json.dumps({
                "name": value.name,
                "bundlePath": value.bundlePath,
                "StartRow" : configValues[value.name].startRow,
                "EndRow" : configValues[value.name].endRow,
                "StartColumn" : configValues[value.name].startColumn,
                "EndColumn" : configValues[value.name].endColumn,   
                "Priority" : configValues[value.name].startOnStartup     
            })
            jsonStr = jsonStr + ","
    jsonStr = jsonStr[:-1]
    jsonStr = jsonStr + "]"
    return jsonStr

def grabCSSList(app):
    cssRepo = CSSRepo.CSSRepo()
    lst= cssRepo.load_css_for_app(app)
    return lst


def loadApp(request, appName):
    appRepo = AppRepo.AppRepo()
    appInfo = appRepo.get_application(appName)
   
    template = loader.get_template('home/app_initialize.html')

    return HttpResponse(template.render({
       "name" : appInfo.name,
       "has_css" : appInfo.hasCSS,
       "cssList" :     grabCSSList(appInfo),
       "bundlePath": appInfo.bundlePath,
    }))