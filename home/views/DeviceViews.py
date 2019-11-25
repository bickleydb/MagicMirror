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


class DeviceViews:

    def __init__(self):
        self.DeviceRepo = DeviceRepo.DeviceRepo()

    def get_device_details(self, deviceId):
        return self.DeviceRepo.load_device_info(deviceId)

    def get_response_with_status_code(self, statusCode, body):
        response = HttpResponse()
        response.status_code = statusCode
        response.content = body
        return response

    @csrf_exempt
    def create_device(self, request):
        if request.method != "POST":
            return self.get_response_with_status_code(400, None)
        device = DeviceModel.from_dictionary(json.loads(request.body))
        device.save()
        device.refresh_from_db()
        contentResponse = DeviceModel.to_dictionary(device)
        response = self.get_response_with_status_code(200, json.dumps(contentResponse))
        response["Set-Cookie"] = "magicMirrorId=" + str(device.deviceId)
        return response

    def load_device_data(self, request):
        if "deviceId" not in request.GET:
            return self.get_response_with_status_code(400, "Require Device Id")
        deviceid = request.GET.get("deviceId")
        deviceDetails = self.get_device_details(deviceid)
        if not deviceDetails:
            return self.get_response_with_status_code(400, "Require Valid Device Id")
        responseContent = DeviceResponse(deviceDetails).to_json()
        return self.get_response_with_status_code(200, responseContent)

    @csrf_exempt
    def login_by_device(self, request):
        if request.method != "POST":
            return self.get_response_with_status_code(400, None)
        if "deviceId" not in request.GET:
            return self.get_response_with_status_code(400, "Require Device Id")
        device = request.GET.get("deviceId")
        user = self.get_user_for_device_id(device)
        login(request, user)
        return self.get_response_with_status_code(200, "")
