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
from MagicMirror.shared.FluentResponseCreator import FluentResponseCreator


class DeviceViews:

    def __init__(self):
        self.DeviceRepo = DeviceRepo.DeviceRepo()

    def get_device_details(self, deviceId):
        return self.DeviceRepo.load_device_info(deviceId)

    @csrf_exempt
    def create_device(self, request):
        responseCreator = FluentResponseCreator()
        if request.method != "POST":
            responseCreator.set_status_code_(400)
            return responseCreator.to_response()
        device = DeviceModel.from_dictionary(json.loads(request.body))
        device.save()
        device.refresh_from_db()
        contentResponse = DeviceModel.to_dictionary(device)
        return responseCreator.set_status_code(200) \
                              .set_content(json.dumps(contentResponse)) \
                              .set_cookie("magicMirrorId", str(device.deviceId), MaxAge=1000000) \
                              .to_response()

    def load_device_data(self, request):
        responseCreator = FluentResponseCreator()
        if "deviceId" not in request.GET:
            return responseCreator.set_status_code(400) \
                                  .set_content("Require device id") \
                                  .to_response()
        deviceid = request.GET.get("deviceId")
        deviceDetails = self.get_device_details(deviceid)
        if not deviceDetails:
            return responseCreator.set_status_code(400) \
                                  .set_content("Require valid device Id") \
                                  .to_response()
        responseContent = DeviceResponse(deviceDetails).to_json()
        return responseCreator.set_status_code(200) \
                              .set_content(responseContent) \
                              .to_response()

    @csrf_exempt
    def login_by_device(self, request):
        responseCreator = FluentResponseCreator()
        if request.method != "POST":
            return responseCreator.set_status_code(400) \
                                  .to_response()
        if "deviceId" not in request.GET:
            return responseCreator.set_status_code(400) \
                                  .set_content("Require device id") \
                                  .to_response()
        device = request.GET.get("deviceId")
        user = self.get_user_for_device_id(device)
        login(request, user)
        return responseCreator.set_status_code(204) \
                              .to_response()
