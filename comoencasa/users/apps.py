from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "comoencasa.users"
    verbose_name = "Usuarios"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
