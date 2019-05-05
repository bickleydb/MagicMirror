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


def get_response_with_status_code(statusCode, body):
    response = HttpResponse()
    response.status_code = statusCode
    response.content = body
    return response


def get_default_user():
    return User.objects.get(username="daniel")


def get_device_details(deviceId):
    return DeviceRepo.DeviceRepo().load_device_info(deviceId)


def get_user_for_device_id(deviceId):
    return UserDeviceRepo.UserDeviceRepo().load_user_by_device_id(deviceId)


def get_user_for_device(device):
    return UserDeviceRepo.UserDeviceRepo().load_user_by_device(device)


@csrf_exempt
def create_device(request):
    if request.method != "POST":
        return get_response_with_status_code(400, None)
    device = DeviceModel.from_dictionary(json.loads(request.body))
    device.save()
    device.refresh_from_db()
    contentResponse = DeviceModel.to_dictionary(device)
    return get_response_with_status_code(200, json.dumps(contentResponse))


def load_device_data(request):
    if "deviceId" not in request.GET:
        return get_response_with_status_code(400, "Require Device Id")
    deviceid = request.GET.get("deviceId")
    deviceDetails = get_device_details(deviceid)
    if not deviceDetails:
        return get_response_with_status_code(400, "Require Valid Device Id")
    responseContent = DeviceResponse(deviceDetails).to_json()
    return get_response_with_status_code(200, responseContent)


def login_by_device(request):
    if "deviceId" not in request.GET:
        return get_response_with_status_code(400, "Require Device Id")
    device = request.GET.get("deviceId")
    user = get_user_for_device_id(device)
    login(request, user)
    return get_response_with_status_code(200, "")


def load_html(request):
    fontList = FontRepo.FontRepo().load_fonts()
    return HttpResponse(HomePageResponse(fontList).to_http())


def load_app_config(request):
    configValue = MMCR.MagicMirrorConfigRepo().load_configuration()
    response_value = MagicMirrorConfigResponse(configValue)
    return HttpResponse(response_value.to_json())


def buildConfigValueDict(appList):
    uiInfo = UICR.UIConfigRepo()
    uiConfigValues = {}
    for app in appList:
        uiConfigList = uiInfo.get_ui_for_app(app)
        if len(uiConfigList) != 0:
            uiConfigValues[app.name] = uiInfo.get_ui_for_app(app)[0].UI_Config
    return uiConfigValues


def getApplicationsForUser(userObj):
    return AppRepo.AppRepo().get_application_list(userObj)


def load_applications(request):
    requestUser = request.user
    if not request.user.is_authenticated:
        requestUser = get_default_user()

    appList = AppRepo.AppRepo().get_application_list(requestUser)
    uiConfigValues = buildConfigValueDict(appList)
    response = AppListResponse(appList, uiConfigValues)
    return HttpResponse(response.to_json())


def grabCSSList(app):
    cssRepo = CSSRepo.CSSRepo()
    return cssRepo.load_css_for_app(app)


def load_app(request, appName):
    appRepo = AppRepo.AppRepo()
    appInfo = appRepo.get_application(appName)
    response = LoadAppResponse(appInfo, grabCSSList(appInfo))
    return HttpResponse(response.to_http_response())
