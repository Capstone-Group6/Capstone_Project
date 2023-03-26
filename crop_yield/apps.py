from django.apps import AppConfig


class CropYieldConfig(AppConfig):
    # This class defines the configuration for the crop_yield app.
    default_auto_field = 'django.db.models.BigAutoField' # Use a BigAutoField as the primary key
    name = 'crop_yield'  # Name of the app (as defined in the project's settings.py)
