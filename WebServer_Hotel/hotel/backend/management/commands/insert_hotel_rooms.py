from django.core.management.base import BaseCommand
from backend.models import Hotel, Hotelrooms

class Command(BaseCommand):
    help = 'Insert HotelRooms data'

    def handle(self, *args, **kwargs):
        try:
            hotel = Hotel.objects.get(id=1)
        except Hotel.DoesNotExist:
            self.stdout.write(self.style.ERROR("Hotel with ID 1 does not exist."))
            return

        tot_rooms = hotel.totrooms  # Es: 60 camere
        room_types = ['Single', 'Double', 'Suite']
        room_status = ['Available', 'Occupied', 'Maintenance']

        inserted = 0

        for i in range(1, tot_rooms + 1):
            # Salta se la camera esiste già
            if Hotelrooms.objects.filter(roomnumber=i, idhotel=hotel).exists():
                self.stdout.write(f"Room {i} already exists.")
                continue

            # Assegna tipo in base alla fascia di camere
            if 1 <= i <= 20:
                room_type = room_types[0] if i % 2 == 0 else room_types[1]  # Single o Double 
            elif 21 <= i <= 40:
                room_type = room_types[0] if i % 2 == 0 else room_types[1]  # Single o Double
            elif 41 <= i <= 60:
                room_type = room_types[2]  # Suite
            else:
                self.stdout.write(self.style.ERROR(f"Room number {i} out of valid range."))
                continue

            # Crea la stanza
            Hotelrooms.objects.create(
                idhotel=hotel,
                roomnumber=i,
                status=room_status[0],  # Available
                type=room_type
            )

            inserted += 1

        self.stdout.write(self.style.SUCCESS(
            f'{inserted} rooms inserted for hotel "{hotel.name}".'
        ))
