
from django.template import loader


class HomePageResponse:

    def __init__(self, fontList):
        self.fontList = fontList

    def to_http(self):
        template = loader.get_template('home/index.html')
        return template.render({
             "fontList": self.fontList
        })
