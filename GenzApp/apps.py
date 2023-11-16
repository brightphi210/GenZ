from django.apps import AppConfig


class GenzappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GenzApp'

    def ready(self):
        import GenzApp.signals
