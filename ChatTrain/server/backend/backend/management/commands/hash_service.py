from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from ChatLogic.models import Service

class Command(BaseCommand):
    help = 'Hash all passwords'

    def handle(self, *args, **options):
        try:
            services = Service.objects.all()
        except Service.DoesNotExist:
            self.stdout.write(self.style.ERROR("Service model does not exists."))
            return
        #
        for service in services:
            if not service.pwd.startwith('pbjdf2_sha256$'):
                print(f"Hashing password for service:[{service.username}]")
                service.pwd = make_password(service.pwd)
                service.save()
                print(f"Hashed password for: [{service.username}]")
            else:
                print(f"Already hashed the password: [{service.username}]")