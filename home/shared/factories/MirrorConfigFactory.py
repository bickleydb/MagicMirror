from home.models.MagicMirrorConfigModel import MagicMirrorConfigModel


class MirrorConfigFactory():

    @staticmethod
    def create_instance(configName, startApp):
        return MagicMirrorConfigModel(
            configurationName=configName,
            startUpApp=startApp,
            rows=5,
            columns=5,
            width_value="1920",
            width_unit="px",
            height_value="1080",
            height_unit="px",
        )
