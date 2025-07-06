# Django imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpRequest
from django.views import View
from django.utils import timezone
from datetime import datetime

# Models
from backend.models import (
    Bigliettoabbonamento,
    Metodopagamento,
    Stazione,
    Tratta,
    Treno,
    Trenostazione,
    Utente
)

# Decorators
from backend.decorators import (
    user_is_logged_in
)

# Logics
# home logic

class HomeLogic(View):
    TEMPLATE = 'Home.html'

    def get(self, request: HttpRequest):
        return render(request, self.TEMPLATE)
    #
    def post(self, request: HttpRequest):
        
        action = request.POST.get('action')

        if action == "buysubscription":
            return self.handle_buysubscription(request)
        elif action == "buyticket":
            return self.handle_buyticket(request)
        else:
            messages.error(request, "Azione non riconosciuta.")
            return redirect('account')
    #
    @user_is_logged_in
    def handle_buysubscription(self, request: HttpRequest):
        print()
    #
    @user_is_logged_in
    def handle_buyticket(self, request: HttpRequest):
        print()
#

@user_is_logged_in
def account(request: HttpRequest):

   # se il codice del decoratore funziona arriva qui e collega alla def
    return render(request, 'Account.html')
#