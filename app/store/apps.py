from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.store"

    def ready(self) -> None:
        from . import signals  # noqa: F401
