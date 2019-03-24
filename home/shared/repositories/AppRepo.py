import home.models.ApplicationDefinitionModel as ApplicationDefinition
import home.models.UserAppListBridgeModel as UALB


class AppRepo:

    """Gets the list of application objects currently in the database
    Returns:
        QuerySet[ApplicationDefinition]
    """

    def get_application_list(self, user):
        appList = UALB.UserAppListBridgeModel.get_manager()
        rtnList = []
        for bridge in appList.filter(user=user):
            rtnList.append(bridge.app)
        return rtnList

    def get_application(self, appName):
        appList = ApplicationDefinition.ApplicationDefinitionModel.get_manager()
        return appList.get(name=appName)

    def load_configuration(self):
        configList = ApplicationDefinition.ApplicationDefinitionModel.get_manager()
        return configList.all()[0]