from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import os

import home.shared.application_repo as repo

def loadHTML(request):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render({
        "fontList" :repo.FontRepo().loadFonts()
    }))


def loadApplications(request):
    appRepo = repo.ApplicationRepo()
    response = HttpResponse(translateAppListToJson(appRepo.get_application_list()))
    return response

def translateAppListToJson(appList):
    jsonStr = "["
    for value in appList:
        jsonStr = jsonStr + json.dumps({
             "name": value.name,
             "bundlePath": value.bundlePath,
             "width" : value.width_value,
             "height" : value.height_value,
        })
        jsonStr = jsonStr + ","
    jsonStr = jsonStr[:-1]
    jsonStr = jsonStr + "]"
    return jsonStr

def grabCSSList(app):
    cssRepo = repo.CSSRepo()
    lst= cssRepo.load_css_for_app(app)
    print(lst)
    return lst


def loadApp(request, appName):
    appRepo = repo.ApplicationRepo()
    appInfo = appRepo.get_application(appName)

    template = loader.get_template('home/app_initialize.html')

    return HttpResponse(template.render({
       "name" : appInfo.name,
       "has_css" : appInfo.hasCSS,
       "cssList" :     grabCSSList(appInfo),
       "bundlePath": appInfo.bundlePath,
    }))