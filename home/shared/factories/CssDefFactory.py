import home.models.CSSResourceModel as CssDef


class CssDefFactory():

    @staticmethod
    def create_instance(cssPath):
        return CssDef.CSSResourceModel(
            sourcePath=cssPath
        )
