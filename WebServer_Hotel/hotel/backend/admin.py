from django.contrib import admin
from backend.models import (
    Events,
    Hotel,
    Hotelrooms,
    Restaurant,
    Restauranttable,
    Roomreservation,
    Tablereservation,
    User
)
# Register your models here.
admin.site.register(Events)
admin.site.register(Hotel)
admin.site.register(Hotelrooms)
admin.site.register(Restaurant)
admin.site.register(Restauranttable)
admin.site.register(Roomreservation)
admin.site.register(Tablereservation)
admin.site.register(User)

