from django.apps import AppConfig


class IrrigationConfig(AppConfig):
    # This class defines the configuration for the irrigation app.
    default_auto_field = 'django.db.models.BigAutoField'  # Use a BigAutoField as the primary key
    name = 'irrigation'  # Name of the app (as defined in the project's settings.py)
