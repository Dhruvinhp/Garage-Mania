from django.apps import AppConfig


class SellerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Seller'

    def ready(self):
        import Seller.signals
