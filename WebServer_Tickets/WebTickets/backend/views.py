# django import
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.tokens import default_token_generator
from django.http import Http404, HttpRequest
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import ListView
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse

# extra import
import os

from backend.models import (
    Bigliettoabbonamento,
    Metodopagamento,
    Stazione,
    Tratta,
    Treno,
    Trenostazione,
    Utente
)

# Class Based View
# InOut Logic
class HomeLogic(View):
    template_name = 'Home.html'

    def get(self, request: HttpRequest):
        return render(request, self.template_name)
    #
    def post(self, request: HttpRequest):
        action = request.POST.get("action")

        if action == 'ticket':
            return self.buy_ticket(request)
        elif action == 'subscription':
            return self.buy_subscription(request)
    #
    def buy_ticket(self, request: HttpRequest):
        if request.method == 'POST':
            partenza = request.POST.get('stazione_partenza')
            arrivo = request.POST.get('stazione_arrivo')
            #
            if partenza == arrivo:
                messages.error(request, "Le stazioni di partenza e arrivo sono identiche")
            else:
                # logica salvataggio dati del biglietto
                print("")
    #
    def buy_subscription(self, request: HttpRequest):
        if request.method == 'POST':
            partenza = request.POST.get('stazione_partenza')
            arrivo = request.POST.get('stazione_arrivo')
            #
            if partenza == arrivo:
                messages.error(request, "Le stazioni di partenza e arrivo sono identiche")
            else:
                # logica salvataggio dati dell'abbonamento
                print("")
    #
#
class UserLogic(View):
    template_name = 'Account.html'
    unlogin_url = 'HomeLogic'

    def get(self, request: HttpRequest):
        return render(request, self.template_name)
    #
    def post(self, request: HttpRequest):
        user_id = request.session.get('user_id')
        if user_id == None:
            print("No user logged in")
            return self.login_view(request)
        else:
            print(f"User logged in: {user_id}")
            return self.account_view(request)
    #
    def login_view(self, request: HttpRequest):
        print("")
    #
    def account_view(self, request: HttpRequest):
        user_id = request.session.get('user_id')
        #
        return render(request, 'Account.html')
    #
    def logout_view(self, request: HttpRequest):
        print("")
    #
    def signup_view(self, request: HttpRequest):
        print("")
    #
#