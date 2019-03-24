import home.models.FontModel as FontModel


class FontRepo:
    def loadFonts(self):
        return FontModel.FontModel.get_manager().all()
