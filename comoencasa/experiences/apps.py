from django.apps import AppConfig


class ExperiencesConfig(AppConfig):
    name = 'experiences'
    verbose_name = 'Experiencias'

    def ready(self):
        try:
            import rooms.signals  # noqa F401
        except ImportError:
            pass