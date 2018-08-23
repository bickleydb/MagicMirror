import home.models.ApplicationUIBridgeModel as ApplicationUIBridge


class UIConfigRepo:
    def get_ui_for_app(self, app):
        return ApplicationUIBridge.ApplicationUIBridgeModel.get_manager().filter(app__id=app.id)
