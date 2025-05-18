from django.contrib.auth.hashers import make_password
from backend.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Cripta le password degli utenti nel db nel modulo User, forse :( '

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        #
        for user in users:
            if not user.Password.startswith('pbkdf2_sha256$'):
                print(f"Criptando la password per l'utente {user.Username}")
                #
                user.Password = make_password(user.Password)
                user.save()
                print(f" Password criptata e salvata per: {user.Username}")
            else: 
                print(f" Password per {user.Username} già criptata e salvata")
#