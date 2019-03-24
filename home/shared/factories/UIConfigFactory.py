from home.models.ApplicationUIConfigModel import \
    ApplicationUIConfigModel as AUM


class UIConfigFactory():

    @staticmethod
    def create_instance(configName):
        return AUM(
            name=configName,
            startRow=0,
            endRow=0,
            startColumn=0,
            endColumn=0,
            startOnStartup=False
        )
