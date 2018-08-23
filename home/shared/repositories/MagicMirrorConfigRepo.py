import home.models.MagicMirrorConfigModel as Config


class MagicMirrorConfigRepo:

    def loadConfiguration(self):
        return Config.MagicMirrorConfigModel.get_manager().all()[0]