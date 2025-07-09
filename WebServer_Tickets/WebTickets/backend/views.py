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
    Utente,
    Trattastazione
)

# Decorators
from backend.decorators import (
    user_is_logged_in
)

# Logics

# Home Page Logic
class HomeLogic(View):
    TEMPLATE = 'Home.html'

    def get(self, request: HttpRequest):
        return render(request, self.TEMPLATE)
    #
    def post(self, request: HttpRequest):
        # show  station
        try:
            stazioni = Stazione.objects.all()
            #
            context = {
                'stazioni': stazioni
            }
        except Exception as e:
            messages.error(f"Problema nel recupero delle stazioni {e}")
        #
        # check for sub or ticket
        action = request.POST.get('action')

        if action == 'subscription':
            return self.handle_buysubscription(request)
        elif action == 'ticket':
            return self.handle_buyticket(request)
        return render(request, self.TEMPLATE, context)
    #
    @user_is_logged_in
    def handle_buysubscription(self, request: HttpRequest):
        return redirect('buypage')
    #
    @user_is_logged_in
    def handle_buyticket(self, request: HttpRequest):
        print('buypage')
#

@user_is_logged_in
def account(request: HttpRequest):
   # se il codice del decoratore funziona arriva qui e collega alla def
    return render(request, 'Account.html')
#
def buypage(request: HttpRequest):
    return render(request, 'BuyPage.html')
#
def logout(request: HttpRequest):
    try: 
        request.session.flush() 
        return render(request, 'Home.html') 
    except: 
        messages.error(request, "Errore durante il logout") 
        return render(request, 'Account.html') 
#
def signup(request: HttpRequest):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        cf = request.POST.get("codicefiscale")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        #
        if not all([name, surname, cf, email, username, password1, password2]):
            messages.error(request, "Errore, tutti i campi devo essere compilati")
            return render(request, 'SignUp.html')
        #
        if password1 != password2:
            messages.error(request, "Errore, le password sono diverse")
            return render(request, 'SignUp.html')
        #
        if Utente.objects.filter(username=username).exists():
            messages.error(request, "Errore, l'username è già in uso")
            return render(request, 'SignUp.html')
        #
        try: 
            hashed_password = make_password(password1)
            # creazione user
            user = Utente.objects.create(
                nome = name,
                cognome = surname,
                codicefiscale = cf,
                email = email,
                username = username,
                password = hashed_password
                )
            #
            messages.success(request, "Utente creato con successo")
            return redirect('login_view')
        except Exception as e:
            messages.error(request, f"Errore, nella creazione dell'utente: {e}")
            return render(request, 'SignUp.html')
        #
    return render(request, 'SignUp.html')
#
def login(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #
        try:
            user = Utente.objects.get(username = username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('account')
            else:
                messages.error(request, "Username o Password errati.")
        except Utente.DoesNotExist:
            messages.error(request, "Utente inesistente.")
    else:
        # aggingere gestione
        print("Request method differente da POST")
    return render(request, 'LogIn.html')
#