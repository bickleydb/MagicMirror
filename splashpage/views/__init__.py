from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from splashpage.shared.repositories.SplashPageRepo import SplashPageRepo
from splashpage.views.SplashScreenResponse import SplashScreenResponse

def loadHTML(request):
    splashPage = SplashPageRepo().load_splash_page()
    response = SplashScreenResponse(splashPage)
    return HttpResponse(response.toHttp())