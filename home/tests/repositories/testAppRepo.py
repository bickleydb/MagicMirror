from django.test import TestCase
from django.contrib.auth.models import User


from home.shared.factories.AppDefFactory import AppDefFactory
from home.shared.repositories.AppRepo import AppRepo
from home.models.ApplicationDefinitionModel import ApplicationDefinitionModel

import home.models.UserAppListBridgeModel as UALB


class EmptyAppRepoTestCase(TestCase):
    def setUp(self):
        self.appRepo = AppRepo()
        User.objects.create_user("test_user")

    def loadTestUser(self):
        return User.objects.get(username="test_user")

    def test_empty_app_list(self):
        self.assertEqual(
            len(self.appRepo.get_application_list(
                self.loadTestUser()
            )), 0)


class AppRepoTestCase(TestCase):
    def load_app(self, appname):
        ApplicationDefinitionModel.get_manager().get(name=appname)

    def load_test_user(self):
        return User.objects.get(username="test_user")

    def setUp(self):
        self.appRepo = AppRepo()

        appList = [
            AppDefFactory.create_instance("test_app_0"),
            AppDefFactory.create_instance("test_app_1"),
            AppDefFactory.create_instance("test_app_2")
        ]

        for app in appList:
            app.save()

        User.objects.create_user("test_user")

        UALB.UserAppListBridgeModel.get_manager().create(
            user=self.load_test_user(),
            app=appList[0]
        )

        UALB.UserAppListBridgeModel.get_manager().create(
            user=self.load_test_user(),
            app=appList[1]
        )

    def test_app_list(self):
        testUser = self.load_test_user()
        appList = self.appRepo.get_application_list(testUser)
        self.assertEqual(len(appList), 2)

    def test_get_app(self):
        app = self.appRepo.get_application("test_app_2")
        self.assertEqual(app.name, "test_app_2")
