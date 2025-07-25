from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpRequest, HttpResponse, Http404
from django.views import View

# Create your views here.
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
        messages.error(f"Error [{e}]")
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
        messages.error(f"Error [{e}]")
    #
#
def resturant_reservation(request: HttpRequest):
    print()
    '''
    qui dentro ci va la logica per la prenotazione dei tavoli e la visualizzazione dei tavoli prenotati e liberi tramite il database
    '''   
#