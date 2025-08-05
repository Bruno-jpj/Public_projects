# django libraries
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpRequest, HttpResponse, Http404
from django.views import View

# models
from backend.models import (
    Events,
    Hotel,
    Hotelrooms,
    Restaurant,
    Restauranttable,
    Roomreservation,
    Tablereservation,
    User
)

# Create your views here.
# login 
def login(request: HttpRequest):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            #
            try:
                user = User.objects.get(Username = username)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    return redirect('home.html')
                else:
                    messages.error(request, "Username o Password errati")
            except User.DoesNotExist:
                messages.error(request, "Username o Password non esistenti")
    except Exception as e:
        print("Error. Login Form")
#
#
def signup(request: HttpRequest):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            mobilephone = request.POST.get("mobilephone")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("pssword2")
            cf = request.POST.get("fiscalcode")
            datebirth = request.POST.get("datebirth")
            cityresidence = request.POST.get("cityresidence")
            streetresidence = request.POST.get("streetresidence")
            #
            if not all([name, surname, mobilephone, username, email, password1, password2, cf, datebirth, cityresidence, streetresidence]):
                messages.error(request, f"Error, Tutti i campi devono essere compilati")
            #
            if password1 != password2:
                messages.error(request, f"Error, le password sono diverse")
                return redirect('signup')
            #
            if User.objects.filter(email=email).exists():
                messages.error(request, "Errore, l'utente già esiste")
                return redirect('signup')
            #
            try:
                hashed_pwd = make_password(password1)
                User.objects.create(
                    name = name,
                    surname = surname,
                    mobilephone = mobilephone,
                    email = email,
                    password = hashed_pwd,
                    fiscalcode = cf,
                    datebirth = datebirth,
                    cityresidence = cityresidence,
                    streetresidence = streetresidence,
                    username = username
                )
                #
                messages.success(request, "utente creato con successo")
                return redirect('login')
            except Exception as e:
                messages.error(request, f"Errore, nella creazione dell'utente")
    except Exception as e:
        messages.error(f"Errore, nel signup {e}")
#
#
def logout(request: HttpRequest):
    try:
        request.session.flush()
        return redirect('HomeLogic')
    except Exception as e:
        messages.error(request, f"Errore durante il logout {e}")
        return redirect('account')
#
# home page view
class HomeLogic(View):
    HOME_TEMPLATE = 'home.html'

    def get(self, request: HttpRequest):
        return render(request, self.HOME_TEMPLATE)
    #
    def post(self, request: HttpRequest):
        try:
            if request.method == "POST":
                
                choice = request.POST.get('redirect')
                
                if choice == 'aboutus':
                    return render(request, 'chisiamo.html')
                elif choice == 'hotel':
                    return render(request, 'hotel.html')
                elif choice == 'resturant':
                    return render(request, 'ristorante.html')
                elif choice == 'events':
                    return render(request, 'eventi.html')
                else:
                    messages.error("Form Error. Please try again.")
        except Exception as e:
            messages.error(f"Error n. {e}")
        #
    #
#
# hotel view
def hotel_view(request: HttpRequest):
    #
    try:
        if request.method == "POST":
            choice = request.POST.get('redirect')
            #
            if choice == 'prenotazione_hotel':
                return render(request, 'prenotazioni_hotel.html')
            #
    except Exception as e:
        messages.error(f"Error [{e}]")
#
def hotel_reservation(request: HttpRequest):
    print()
    '''
    qui dentro ci va la logica per la prenotazione delle camere e la visualizzazione delle camere prenotate e libere tramite il database
    '''   
#
# events view
def events_view(request: HttpRequest):
    try:
        if request.method == "POST":
            choice = request.POST.get('redirect')
            #
            if choice == 'prenotazione_hotel':
                return render(request, 'prenotazioni_eventi.html')
            #
    except Exception as e:
        messages.error(request, f"Error [{e}]")
    #
#
#
def events_reservation(request: HttpRequest):
    print()
    '''
    qui dentro ci va la logica per vedere solo la disponibilità della location e inserire la richiesta di prenotazione nel database
    '''   
#
# resturant view
def resturant_view(request: HttpRequest):
    try:
        if request.method == "POST":
            choice = request.POST.get('redirect')
            #
            if choice == 'prenotazione_hotel':
                return render(request, 'prenotazioni_ristorante.html')
            #
    except Exception as e:
        messages.error(request, f"Error [{e}]")
    #
#
#
def resturant_reservation(request: HttpRequest):
    print()
    '''
    qui dentro ci va la logica per la prenotazione dei tavoli e la visualizzazione dei tavoli prenotati e liberi tramite il database
    '''   
#
