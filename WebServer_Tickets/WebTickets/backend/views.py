# Django imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpRequest
from django.views import View

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

# Logics

# home logic
class HomeLogic(View):

    TEMPLATE = 'Home.html'

    def get(self, request: HttpRequest):
        return render(request, self.TEMPLATE)
    #
    def post(self, request: HttpRequest):

        # user in session
        user_id = request.session.get('user_id')

        # check user in session
        if user_id != None:
            print(f"User logged in session is {user_id}")

        action = request.POST.get('action')
        try:
            if action == "buysubscription":
                return self.buysubscription(request)
            elif action == "buyticket":
                return self.buyticket(request)
            else:
                print("Errore. Gestione action form html")
        except Exception as e:
            print(f"Errore. try-except action form")
    #
    def buysubscription(self, request: HttpRequest):
        print("")
    #
    def buyticket(self, request: HttpRequest):
        print("")
    #
#