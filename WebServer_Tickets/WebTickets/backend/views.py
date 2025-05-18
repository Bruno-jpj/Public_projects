from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.hashers import check_password, make_password
#
from .models import (
    Biglietto,
    Metodopagamento,
    Stazione,
    Tratta,
    Treno,
    Trenostazione,
    Utente,
)

# view to find a specific station
def find_station_view(request):
    stazione = None  # inizializza la variabile
    if request.method == "POST":
        nome = request.POST.get("nome")
        try:
            stazione = Stazione.objects.get(nome=nome)
        except Stazione.DoesNotExist:
            messages.error(request, "Stazione non trovata")
    #
    if stazione:
        print(f"Stazione cercata: {stazione}")
        return render(request, "find_station.html", {"Stazione": stazione})
    else:
        return render(request, "find_station.html")
#
# view of the account page
def account_view(request):
    if 'user_id' not in request.session:
        return redirect('login_view')
    #
    user_id = request.session['user_id']
    #
    