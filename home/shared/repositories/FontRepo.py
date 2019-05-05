import home.models.FontModel as FontModel


class FontRepo:
    def load_fonts(self):
        return FontModel.FontModel.get_manager().all()
