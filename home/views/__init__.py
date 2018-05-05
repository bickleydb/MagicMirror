from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from home.shared.repositories import AppRepo, CSSRepo, FontRepo, UIConfigRepo, MagicMirrorConfigRepo
from home.views.responses.MagicMirrorConfigResponse import MagicMirrorConfigResponse
from home.views.responses.AppListResponse import AppListResponse
from home.views.responses.LoadAppResponse import LoadAppResponse
from home.views.responses.HomePageResponse import HomePageResponse

def loadHTML(request):
    fontList = FontRepo.FontRepo().loadFonts()
    return HttpResponse(HomePageResponse(fontList).toHttp())


def loadAppConfig(request):
    configValue = MagicMirrorConfigRepo.MagicMirrorConfigRepo().loadConfiguration()
    response_value = MagicMirrorConfigResponse(configValue)
    return HttpResponse(response_value.toJSON())

def buildConfigValueDict(appList):
    uiInfo = UIConfigRepo.UIConfigRepo()
    uiConfigValues = {}
    for app in appList:
        uiConfigList = uiInfo.get_ui_for_app(app)
        if len(uiConfigList) != 0:
            uiConfigValues[app.name] = uiInfo.get_ui_for_app(app)[0].UI_Config
    return uiConfigValues

def loadApplications(request):
    appList = AppRepo.AppRepo().get_application_list()
    uiConfigValues = buildConfigValueDict(appList)
    response = AppListResponse(appList,uiConfigValues)
    return HttpResponse(response.toJSON())

def grabCSSList(app):
    cssRepo = CSSRepo.CSSRepo()
    lst= cssRepo.load_css_for_app(app)
    return lst

def loadApp(request, appName):
    appRepo = AppRepo.AppRepo()
    appInfo = appRepo.get_application(appName)
    response = LoadAppResponse(appInfo,grabCSSList(appInfo))
    return HttpResponse(response.toHttpResponse())