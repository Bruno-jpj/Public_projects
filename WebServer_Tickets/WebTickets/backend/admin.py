from django.contrib import admin
from backend.models import *
#
#admin.site.refister([Bigliettoabbonamento, Metodopagamento, Stazione, Tratta, Trattastazione, Treno, Trenostazione, Utente])
'''
'''
admin.site.register(Bigliettoabbonamento)
admin.site.register(Metodopagamento)
admin.site.register(Stazione)
admin.site.register(Tratta)
admin.site.register(Trattastazione)
admin.site.register(Treno)
admin.site.register(Trenostazione)
admin.site.register(Utente)