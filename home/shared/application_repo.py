import home.models.ApplicationModel as models


class ApplicationRepo:


    """Gets the list of application objects currently in the database
    
    Returns:
        QuerySet[ApplicationDefinition]
    """

    def get_application_list(self):
        appList = models.ApplicationDefinition.get_manager()
        return appList.all()

    def get_application(self, appName):
        appList = models.ApplicationDefinition.get_manager()
        return appList.get(name=appName)

class CSSRepo:
    def load_css_for_app(self, app):
        return models.AppCSSFiles.get_manager().all().filter(actualApp__id=app.id)
        
class FontRepo:
    def loadFonts(self):
        return models.Fonts.get_manager().all()