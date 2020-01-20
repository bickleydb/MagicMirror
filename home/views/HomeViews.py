from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json.encoder

from home.shared.repositories import \
    AppRepo, \
    CSSRepo, \
    FontRepo, \
    UIConfigRepo as UICR, \
    MagicMirrorConfigRepo as MMCR, \
    DeviceRepo as DeviceRepo, \
    UserDeviceRepo as UserDeviceRepo

from home.views.responses.MagicMirrorConfigResponse \
    import MagicMirrorConfigResponse
from home.views.responses.AppListResponse import AppListResponse
from home.views.responses.LoadAppResponse import LoadAppResponse
from home.views.responses.HomePageResponse import HomePageResponse
from home.views.responses.DeviceResponse import DeviceResponse
from home.models.Device import DeviceModel
from django.views.decorators.csrf import csrf_exempt


class HomeViews():

    def __init__(self):
        self.userDeviceRepo = UserDeviceRepo.UserDeviceRepo()
        self.magicMirrorRepo = MMCR.MagicMirrorConfigRepo()
        self.appRepo = AppRepo.AppRepo()
        self.cssRepo = CSSRepo.CSSRepo()
        self.fontRepo = FontRepo.FontRepo()

    def get_response_with_status_code(self, statusCode, body):
        response = HttpResponse()
        response.status_code = statusCode
        response.content = body
        return response

    def get_default_user(self):
        currentConfig = self.magicMirrorRepo.load_configuration()
        if(currentConfig.default_user is not None):
            return currentConfig.default_user
        return User.objects.get(username="daniel")

    def get_user_for_device_id(self, deviceId):
        return self.userDeviceRepo.load_user_by_device_id(deviceId)

    def get_user_for_device(self, device):
        return self.userDeviceRepo.load_user_by_device(device)

    def load_html(self, request):
        fontList = self.fontRepo.load_fonts()
        return HttpResponse(HomePageResponse(fontList).to_http())

    def load_app_config(self, request):
        configValue = self.magicMirrorRepo.load_configuration()
        response_value = MagicMirrorConfigResponse(configValue)
        return HttpResponse(response_value.to_json())

    def buildConfigValueDict(self, appList):
        uiInfo = UICR.UIConfigRepo()
        uiConfigValues = {}
        for app in appList:
            uiConfigList = uiInfo.get_ui_for_app(app)
            if len(uiConfigList) != 0:
                config = uiInfo.get_ui_for_app(app)[0].UI_Config
                uiConfigValues[app.name] = config
        return uiConfigValues

    def getApplicationsForUser(self, userObj):
        return self.appRepo.get_application_list(userObj)

    def load_applications(self,  request):
        requestUser = request.user
        if not request.user.is_authenticated:
            requestUser = self.get_default_user()
        appList = self.appRepo.get_application_list(requestUser)
        uiConfigValues = self.buildConfigValueDict(appList)
        response = AppListResponse(appList, uiConfigValues)
        return HttpResponse(response.to_json())

    def grabCSSList(self, app):
        return self.cssRepo.load_css_for_app(app)

    def load_app(self, request, appName):
        appInfo = self.appRepo.get_application(appName)
        response = LoadAppResponse(appInfo, self.grabCSSList(appInfo))
        return HttpResponse(response.to_http_response())
