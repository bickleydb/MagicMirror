import splashpage.models.SplashPageModel as SplashPageModel

class SplashPageRepo:
    def load_splash_page(self):
        return SplashPageModel.SplashPageModel.get_manager().all()[0]
        