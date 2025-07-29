from django.core.management.base import BaseCommand
from backend.models import Restauranttable, Restaurant

class Command(BaseCommand):
    # Descrizione del comando, visibile con `python manage.py help`
    help = 'Insert RestaurantTable data'

    def handle(self, *args, **kwargs):
        try:
            # Recupera il ristorante con ID 1 dal database
            restaurant = Restaurant.objects.get(id=1)
        except Restaurant.DoesNotExist:
            # Se non esiste, stampa errore e interrompe il comando
            self.stdout.write(self.style.ERROR("Restaurant with ID 1 does not exist."))
            return

        # Numero totale di tavoli da creare, preso dal modello Restaurant
        tot_tables = restaurant.tottables # -> 30

        # Posizioni fisse per i tavoli
        position_1 = 'Inside'
        position_2 = 'Outside'

        # Stato iniziale dei tavoli (disponibili)
        status = 'Available'

        # Contatore di quanti tavoli sono stati effettivamente inseriti
        inserted = 0

        # Cicla da 1 fino a tot_tables inclusi
        for i in range(1, tot_tables + 1):

            # Verifica se esiste già un tavolo con lo stesso numero per questo ristorante
            if Restauranttable.objects.filter(tablenumber=i, idrestaurant=restaurant).exists():
                self.stdout.write(f'Table {i} already exists.')
                continue  # salta alla prossima iterazione

            # Assegna la posizione: metà tavoli dentro, metà fuori
            position = position_1 if i <= tot_tables // 2 else position_2

            # Crea il tavolo nel database
            Restauranttable.objects.create(
                idrestaurant=restaurant,  # chiave esterna al ristorante
                status=status,            # disponibile
                position=position,        # dentro o fuori
                tablenumber=i             # numero progressivo
            )
            inserted += 1  # incrementa il contatore di tavoli creati

        # Messaggio finale di successo
        self.stdout.write(self.style.SUCCESS(
            f'{inserted} tables inserted for restaurant "{restaurant.name}".'
        ))
