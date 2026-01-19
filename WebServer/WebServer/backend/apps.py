from django.apps import AppConfig

# è usato per configurare e gestire la tua app Django.
class BackendConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    # name è obbligatorio e rappresenta il percorso della tua app.
    name = 'backend'
    #
    def ready(self):
        #
        import backend.signals
