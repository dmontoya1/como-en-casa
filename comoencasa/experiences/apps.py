from django.apps import AppConfig


class ExperiencesConfig(AppConfig):
    name = 'experiences'

    def ready(self):
        try:
            import rooms.signals  # noqa F401
        except ImportError:
            pass