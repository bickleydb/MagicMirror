import home.models.MagicMirrorConfigModel as Config


class MagicMirrorConfigRepo:

    def loadConfiguration(self):
        allModels = Config.MagicMirrorConfigModel.get_manager().all()
        return Config.MagicMirrorConfigModel.get_manager().all()[0]