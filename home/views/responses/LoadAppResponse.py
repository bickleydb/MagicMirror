from django.template import loader


class LoadAppResponse:

    def __init__(self, appInfo, cssList):
        self.appInfo = appInfo
        self.cssList = cssList

    def to_http_response(self):
        template = loader.get_template('home/app_initialize.html')
        return template.render({
            "name": self.appInfo.name,
            "has_css": self.appInfo.hasCSS,
            "cssList": self.cssList,
            "bundlePath": self.appInfo.bundlePath,
        })
