from django.apps import AppConfig


class RecommendationModelConfig(AppConfig):
    # Specifies the default auto field for the models in the app
    default_auto_field = 'django.db.models.BigAutoField'

    # Specifies the name of the app
    name = 'recommendation_model'
