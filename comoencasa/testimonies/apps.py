from django.apps import AppConfig


class TestimoniesConfig(AppConfig):
    name = 'testimonies'
    verbose_name = "Testimonios"

    def ready(self):
        try:
            import testimonies.signals  # noqa F401
        except ImportError:
            pass

