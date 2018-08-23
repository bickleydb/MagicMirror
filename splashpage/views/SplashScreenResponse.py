from django.shortcuts import render
from django.template import loader

class SplashScreenResponse:

    def __init__(self, splashPage):
        self.splashPage = splashPage

    def toHttp(self):
        template = loader.get_template('splashpage/index.html')
        return template.render({
            "uses_animation" : self.splashPage.UseAnimation,
            "splash_svg" : self.splashPage.SVGField,
            "color_string" : self.splashPage.BackgroundColorString,
        })
