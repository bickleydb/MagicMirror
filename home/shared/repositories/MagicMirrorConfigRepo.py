import home.models.MagicMirrorConfigModel as Config


class MagicMirrorConfigRepo:

    def load_configuration(self):
        allModels = Config.MagicMirrorConfigModel.get_manager().all()
        if len(allModels) == 0:
            return None
        return Config.MagicMirrorConfigModel.get_manager().all()[0]
