from django.apps import AppConfig


# This class represents the configuration of the 'accounts' app
class AccountsConfig(AppConfig):
    # This attribute specifies the default auto field to be used for models that do not explicitly define one
    default_auto_field = 'django.db.models.BigAutoField'
    # This attribute specifies the name of the app
    name = 'accounts'
