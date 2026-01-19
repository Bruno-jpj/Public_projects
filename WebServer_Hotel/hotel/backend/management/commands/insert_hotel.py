from django.core.management.base import BaseCommand
from backend.models import Hotel

class Command(BaseCommand):
    help = 'Insert Hotel data'

    def __init__(self):
        super().__init__()
        self.NAME = 'Il Castagno'
        self.CITY = 'Orciano di Pesaro'
        self.STREET = 'Corso Matteotti 72'
        self.PHONE = '0721 977672'
        self.EMAIL = 'info@ilcastango.it'
        self.TOTALROOMS = 60 # 101 -> 120, 121 -> 140, 141 -> 160
    
    def handle(self, *args, **kwargs):
        # check if exists, to not duplicate
        if Hotel.objects.filter(name=self.NAME).exists():
            self.stdout.write(f'Hotel "{self.NAME}" already exists.')
            return
        
        # create the hotel instance
        h = Hotel.objects.create(
            name=self.NAME,
            city=self.CITY,
            street=self.STREET,
            phone=self.PHONE,
            email=self.EMAIL,
            totrooms=self.TOTALROOMS
        )
        
        self.stdout.write(self.style.SUCCESS(f'Hotel "{h.name}" inserted successfully.'))