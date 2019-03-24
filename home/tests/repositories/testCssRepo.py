from django.test import TestCase
from django.contrib.auth.models import User
from home.shared.repositories.CSSRepo import CSSRepo
from home.shared.factories.AppDefFactory import AppDefFactory
from home.shared.factories.CssDefFactory import CssDefFactory
from home.models.ApplicationDefinitionModel import ApplicationDefinitionModel
from home.models.CSSResourceModel import CSSResourceModel
from home.models.ApplicationCSSFileBridgeModel import \
    ApplicationCSSFileBridgeModel


class CssRepoTestCase(TestCase):
    def setUp(self):

        self.cssRepo = CSSRepo()

        self.appList = [
            AppDefFactory.create_instance("test_app_0"),
            AppDefFactory.create_instance("test_app_1"),
            AppDefFactory.create_instance("test_app_2")
        ]

        for app in self.appList:
            app.save()

        self.cssResourceList = [
            CssDefFactory.create_instance("path0"),
            CssDefFactory.create_instance("path1"),
            CssDefFactory.create_instance("path2"),
        ]

        for css in self.cssResourceList:
            css.save()

        ApplicationCSSFileBridgeModel.get_manager().create(
            actualApp=self.appList[0],
            css_resource=self.cssResourceList[0]
        )

        ApplicationCSSFileBridgeModel.get_manager().create(
            actualApp=self.appList[1],
            css_resource=self.cssResourceList[0]
        )
        ApplicationCSSFileBridgeModel.get_manager().create(
            actualApp=self.appList[1],
            css_resource=self.cssResourceList[1]
        )
        return super().setUp()

    def testEmptyApp(self):
        retrievedVal = self.cssRepo.load_css_for_app(self.appList[2])
        self.assertEqual(0, len(retrievedVal))

    def testSingleCssResource(self):
        retrievedVal = self.cssRepo.load_css_for_app(self.appList[0])
        self.assertEqual(1, len(retrievedVal))

    def testMultipleCssResource(self):
        retrievedVal = self.cssRepo.load_css_for_app(self.appList[1])
        self.assertEqual(2, len(retrievedVal))
