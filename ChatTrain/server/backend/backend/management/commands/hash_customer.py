from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from ChatLogic.models import Customers

class Command(BaseCommand):
    help = 'Hash all passwords'

    def handle(self, *args, **options):
        try:
            customers = Customers.objects.all()
        except Customers.DoesNotExist:
            self.stdout.write(self.style.ERROR("Customer model does not exists."))
            return
        #
        for customer in customers:
            if not customer.pwd.startswith('pbkdf2_sha256$'):
                print(f"Hashing password for customer:[{customer.username}]")
                customer.pwd = make_password(customer.pwd)
                customer.save()
                print(f"Hashed password for: [{customer.username}]")
            else:
                print(f"Already hashed the password: [{customer.username}]")