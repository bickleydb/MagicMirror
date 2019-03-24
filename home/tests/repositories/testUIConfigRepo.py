from django.test import TestCase
from django.contrib.auth.models import User
from home.models.ApplicationUIBridgeModel import ApplicationUIBridgeModel as AUB
from home.models.ApplicationDefinitionModel import ApplicationDefinitionModel as AppDef
from home.models.ApplicationUIConfigModel import ApplicationUIConfigModel as AUI
from home.shared.factories.AppDefFactory import AppDefFactory
from home.shared.factories.UIConfigFactory import UIConfigFactory
from home.shared.repositories.UIConfigRepo import UIConfigRepo


class EmptyConfigRepo(TestCase):

    def setUp(self):
        self.app = AppDefFactory.create_instance("test")

    def testEmpty(self):
        self.assertEqual(len(UIConfigRepo().get_ui_for_app(self.app)), 0)

class RegularConfigRepo(TestCase):

    def setUp(self):
        
        self.appList = [
            AppDefFactory.create_instance("test_0"),
            AppDefFactory.create_instance("test_1"),
            AppDefFactory.create_instance("test_2")
        ]

        for app in self.appList:
            app.save()
        
        self.config = UIConfigFactory.create_instance("fake_config")
        self.config.save()

        AUB(
            app=self.appList[0],
            UI_Config=self.config
        ).save()

    def testAtLeastOne(self):
        self.assertTrue(UIConfigRepo().get_ui_for_app(self.appList[0]))
