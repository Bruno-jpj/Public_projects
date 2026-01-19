from django.core.management.base import BaseCommand
from backend.models import Restaurant
import datetime

class Command(BaseCommand):
    help = 'Insert data into the Restaurant model'

    def __init__(self):
        super().__init__()
        self.NAME = 'Il Castagno'
        self.CITY = 'Orciano di Pesaro'
        self.STREET = 'Corso Matteotti 72'
        self.CLOSINGDAYS = 'Monday'
        self.OPENINGDAYS = 'Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday'
        self.CLOSINGTIME = datetime.time(23, 0)
        self.OPENINGTIME = datetime.time(11, 30)
        self.PHONE = '0721 977672'
        self.EMAIL = 'info@ilcastagno.it'
        self.TOTALTABLES = 30

    def handle(self, *args, **kwargs):
        # check if exists, to not duplicate
        if Restaurant.objects.filter(name=self.NAME).exists():
            self.stdout.write(f'Restaurant "{self.NAME}" already exists.')
            return
        #
        r = Restaurant.objects.create(
            name = self.NAME,
            city = self.CITY,
            street = self.STREET,
            closingdays = self.CLOSINGDAYS,
            openingdays = self.OPENINGDAYS,
            closingtime = self.CLOSINGTIME,
            openingtime = self.OPENINGTIME,
            phone = self.PHONE,
            email = self.EMAIL,
            tottables = self.TOTALTABLES
        )
        #
        self.stdout.write(self.style.SUCCESS(f'Ristorante "{r.name}" inserito con successo.'))
#   