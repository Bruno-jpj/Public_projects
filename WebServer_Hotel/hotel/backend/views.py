from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpRequest, HttpResponse, Http404
from django.views import View

# Create your views here.
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
def hotel_reservation(request: HttpRequest):
    HOTEL_TEMPLATE = 'hotel.html'
    #
    try:
        if request.method == "POST":
            name = request.POST.get('redirect')
            if name == 'prenotazione_hotel':
                return render(request, 'prenotazioni.html')
    except Exception as e:
        messages.error(f"Error in reservation btn. {e}")
    return render(request, HOTEL_TEMPLATE)
#
def events_reservation(request: HttpRequest):
    EVENTS_TEMPLATE = 'eventi.html'
    #
    try:
        if request.method == "POST":
            name = request.POST.get('redirect')
            if name == 'prenotazione_eventi':
                return render(request, 'prenotazioni.html')    
    except Exception as e:
        messages.error(f"Error in events btn {e}")
    return render(request, EVENTS_TEMPLATE)
#
def resturant_reservation(request: HttpRequest):
    EVENTS_TEMPLATE = 'ristorante.html'
    #
    try:
        if request.method == "POST":
            name = request.POST.get('redirect')
            if name == 'prenotazione_ristorante':
                return render(request, 'prenotazioni.html')    
    except Exception as e:
        messages.error(f"Error in events btn {e}")
    return render(request, EVENTS_TEMPLATE)
#