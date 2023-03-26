from django.apps import AppConfig


class FertilizerReqConfig(AppConfig):
    # This class defines the configuration for the fertilizer_req app.
    default_auto_field = 'django.db.models.BigAutoField'  # Use a BigAutoField as the primary key
    name = 'fertilizer_req'  # Name of the app (as defined in the project's settings.py)
