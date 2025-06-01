from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404, HttpRequest
from django.contrib.auth.hashers import check_password, make_password
#
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
#
from backend.forms import PasswordResetRequestForm, SetNewPasswordForm
#
from backend.models import (
    Bigliettoabbonamento, 
    Metodopagamento,
    Stazione,
    Tratta,
    Treno,
    Trenostazione,
    Utente
    )
#
# view of the login
def login_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #
        try:
            user = Utente.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect("account_view")
            else:
                messages.error(request, "Username o Password errati!")
        except Utente.DoesNotExist:
            messages.error(request, "Username o Password inesistenti")
    return render(request, 'LogIn.html')
#
# view for sign up
def signup_view(request: HttpRequest):
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
# view for the log out
def log_out_view(request: HttpRequest):
    try: 
        request.session.flush() 
        return render(request, 'Home.html') 
    except: 
        messages.error(request, "Errore durante il logout") 
        return render(request, 'Account.html') 
#
# view for home
def home_view(request: HttpRequest):
    user_id = request.session.get('user_id')
    print(f"{user_id}")
    return render(request, 'Home.html')
#
# view to find a specific station
def find_station_view(request: HttpRequest):
    return render(request, 'FindStation.html')

#
# view for the account info
def account_view(request: HttpRequest):
    user_id = request.session.get('user_id')
    print(user_id)
    #
    if not user_id:
        return redirect('login_view')
    #
    try:
        user = Utente.objects.get(id=user_id)
    except Utente.DoesNotExist:
        return redirect('login_view')
    #
    context = {
        'user': user
    }
    return render(request, 'Account.html', context)
#
# view for the info
def info_view(request: HttpRequest):
    return render(request, 'Info.html')
#
# view for the tickets
#
# view for the offers
#
# view for the news