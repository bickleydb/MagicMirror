import home.models.ApplicationUIBridgeModel as AUB


class UIConfigRepo:
    def get_ui_for_app(self, app):
        manager = AUB.ApplicationUIBridgeModel.get_manager()
        return manager.filter(app__id=app.id)
