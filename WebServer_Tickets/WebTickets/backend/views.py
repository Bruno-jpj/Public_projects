from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.hashers import check_password, make_password
from django.core.management.base import BaseCommand
#
from backend.models import (
    Biglietto, 
    Metodopagamento,
    Stazione,
    Tratta,
    Treno,
    Trenostazione,
    Utente
    )
#
# view of the login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #
        try:
            user = Utente.objects.get(username=username)

            if check_password(password, user.pwd):
                request.session['user_id'] = user.id
                return redirect("account_view")
            else:
                messages.error(request, "Username o Password errati!")
        except Utente.DoesNotExist:
            messages.error(request, "Username o Password inesistenti")
    else:
        messages.error(request, "Errore nel metodo")
#
# view for sign up
def signup_view(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            cf = request.POST.get("codicefiscale")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            #
            if not name or not surname or not cf or not email or not username or not password1 or not password2:
                messages.error(request, "Errore, tutti i campi devo essere compilati")
            if password1 != password2:
                messages.error(request, "Errore, le password sono diverse")
        except:
            messages.error(request, "Qualcosa è andato storto")
        #
        password1 = make_password(password1)
        #
        try: 
            # creazione user
            user = Utente.objects.create(
                nome = name,
                cognome = surname,
                codicefiscale = cf,
                email = email,
                username = username,
                pwd = password1
            )
        except:
            messages.error(request, "Errore, nella creazione dell'utente")
        #
        messages.success(request, "Utente creato con successo")
        return redirect("login_view")
    else:
        messages.error(request, "Errore nel metodo")
#
# view for the log out
def log_out_view(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('login_view')
#
# view to find a specific station
def find_station_view(request):
    if request.method == "POST":
        #
        nome = request.POST.get("nome")
        citta = request.POST.get("citta")
        #
        if not nome or not citta:
            messages.error(request, "Errore, campo mancante")
            #
        try:
            town = Stazione.objects.get(citta=citta)
            name = Stazione.objects.get(nome=nome)
            #
            messages.success("Stazione trovata con successo")
            #
            return render() # ritorna la stazione
            #
        except Stazione.DoesNotExist:
            messages.error(request, "La stazione non esiste, ricontrolla i campi")
        except Stazione.MultipleObjectsReturned:
            messages.info("Piu stazioni trovate")
        except:
            messages.error(request, "Errore")   
    else:
        messages.error(request, "Errore nel metodo")      
#
# view for the account info
def account_view(request):
    if 'user_id' not in request.session:
        return redirect('login_view')
    #
    user_id = request.session['user_id']
    #
    try:
        user = Utente.objects.get(id=user_id)
    except Utente.DoesNotExist:
        return redirect('login_index_view')
    #
    print(f"User nella home page: [{user}]")
    #
    return render(request, 'Account.html', {'user': user})
#
# view for the info
def info_view(request):
    if 'user_id' not in request.session:
        return redirect('login_view')
    #
    