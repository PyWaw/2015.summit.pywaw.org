from django import apps


class AppConfig(apps.AppConfig):
    name = 'registration'

    def ready(self):
        import registration.signals