from django.test import TestCase
from django.contrib.auth.models import User


from home.shared.repositories.MagicMirrorConfigRepo import \
    MagicMirrorConfigRepo as MCR
from home.models.MagicMirrorConfigModel import MagicMirrorConfigModel
from home.models.ApplicationDefinitionModel import ApplicationDefinitionModel \
    as AppDef
from home.shared.factories.AppDefFactory import AppDefFactory
from home.shared.factories.MirrorConfigFactory  \
    import MirrorConfigFactory as MCF


class EmptyMirrorConfigTest(TestCase):
    def testEmptyMirrorConfig(self):
        self.assertEqual(MCR().load_configuration(), None)


class SingleMirrorConfigTest(TestCase):
    def setUp(self):
        self.appList = [
            AppDefFactory.create_instance("test_app_0"),
        ]

        for app in self.appList:
            app.save()

        config = MCF.create_instance("TestConfig", self.appList[0])
        config.save()

    def testLoadConfig(self):
        self.assertNotEqual(MCR().load_configuration(), None)
