import home.models.ApplicationCSSFileBridgeModel as AppCSSBridge


class CSSRepo:
    def load_css_for_app(self, app):
        return AppCSSBridge.ApplicationCSSFileBridgeModel.get_manager().all().filter(actualApp__id=app.id)


class CSSRepo:
    def load_css_for_app(self, app):
        return AppCSSBridge.ApplicationCSSFileBridgeModel.get_manager().all().filter(actualApp__id=app.id)