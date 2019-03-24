
import home.models.ApplicationDefinitionModel as AppDef


class AppDefFactory():

    @staticmethod
    def create_instance(appName):
        return AppDef.ApplicationDefinitionModel(
            name=appName,
            bundlePath="",
            width_value=0,
            height_value=0,
            width_unit='cm',
            height_unit='cm',
            hasCSS=True
        )
