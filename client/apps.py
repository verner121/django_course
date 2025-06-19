from django.apps import AppConfig


class ClientConfig(AppConfig):
    """ Класс для конфигурационного названия """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'client'
