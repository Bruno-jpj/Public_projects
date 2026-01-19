# django libraries
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpRequest, HttpResponse, Http404
from django.views import View

from datetime import datetime, date

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
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                messages.error(request, "Username o Password errati")
        except User.DoesNotExist:
            messages.error(request, "Username o Password inesistenti")

        return redirect('login')

    return render(request, 'login.html')
# signup
def signup(request: HttpRequest):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            mobilephone = request.POST.get("mobilephone")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            cf = request.POST.get("fiscalcode")
            datebirth = request.POST.get("datebirth")
            cityresidence = request.POST.get("cityresidence")
            streetresidence = request.POST.get("streetresidence")
            #
            if not all([name, surname, mobilephone, username, email, password1, password2, cf, datebirth, cityresidence, streetresidence]):
                messages.error(request, f"Error, Tutti i campi devono essere compilati")
                return redirect('signup')
            #
            if password1 != password2:
                messages.error(request, f"Error, le password sono diverse")
                return redirect('signup')
            #
            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
                messages.error(request, "Utente già esistente.")
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
        messages.error(request, f"Errore, nel signup {e}")
    #
    return render(request, 'signup.html')
# logout
def logout(request: HttpRequest):
    try:
        request.session.flush()
        return redirect('home') # home = HomeLogic
    except Exception as e:
        messages.error(request, f"Errore durante il logout {e}")
        return redirect('account')
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
                    return redirect('aboutus_view')
                elif choice == 'hotel':
                    return redirect('hotel_view')
                elif choice == 'resturant':
                    return redirect('restaurant_view')
                elif choice == 'events':
                    return redirect('events_view')
                elif choice == 'login':
                    return redirect('login')
                elif choice == 'signup':
                    return redirect('signup')
                else:
                    messages.error(request, "Form Error. Please try again.")
                    return render(request, 'HomeLogic')
        except Exception as e:
            messages.error(request, f"Error n. {e}")
        #
        return redirect('home')
    #
# about us redirect 
def aboutus_view(request: HttpRequest):
    try:
        if request.method == "POST":
            choice = request.POST.get('redirect')
            if choice == 'aboutus':
                return render(request, 'chisiamo.html')
    except Exception as e:
        print(f"Errore: redirect aboutus")
    return redirect('home')
# hotel redirect
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
        messages.error(request, f"Error [{e}]")
    #
    return render(request, 'hotel.html')
# hotel room reservation view
def hotel_reservation(request: HttpRequest):

    # get the hotel info
    ObjHotel = get_object_or_404(Hotel, id=1)

    # get all the rooms in the hotel ordered by roomnumber where the idhotel is equal to the id of the hotel(1)
    ObjRoom = Hotelrooms.objects.filter(idhotel=ObjHotel).order_by('roomnumber')

    if request.method == "POST":
        
        # btn to reserve a room
        reservation = request.POST.get('redirect')
        
        # get the user choices in the html
        room_id = request.POST.get('room_id') 
        checkin_str = request.POST.get("checkindate")
        checkout_str = request.POST.get("checkoutdate")
        peoplenumber = request.POST.get("peoplenumber")
        notes = request.POST.get("notes")

        # check when user click on reservation 
        if reservation == "reservation":

            # check if user is logged in
            user_id = request.session.get('user_id')
            if not user_id:
                messages.warning(request, "Devi effettuare il login per prenotare.")
                return redirect('login')

            # check user exist
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                messages.error(request, "Errore: utente non trovato.")
                return redirect('login')

            # check if the room chosen is free
            try:
                room = Hotelrooms.objects.get(id=room_id, status='available')
            except Hotelrooms.DoesNotExist:
                messages.error(request, "Errore: la stanza non è disponibile.")
                return redirect('hotel_reservation')

            # check if all the fields were chosen
            if not all([checkin, checkout, peoplenumber, room_id]):
                messages.error(request, "Tutti i campi devono essere compilati.")
                return redirect('hotel_reservation')

            # check if checkin and checkout are correct
            try:
                checkin = datetime.strptime(checkin_str, "%Y-%m-%d").date()
                checkout = datetime.strptime(checkout_str, "%Y-%m-%d").date()
            except ValueError:
                messages.error(request, "Formato data non valido.")
                return redirect('hotel_reservation')

            if checkout <= checkin:
                messages.error(request, "Errore: il checkout deve essere almeno un giorno dopo il check-in.")
                return redirect('hotel_reservation')

            # create the reservation
            try:
                # create reservation
                Roomreservation.objects.create(
                    iduser=user,
                    idhotelroom=room,
                    checkindate=checkin,
                    checkoutdate=checkout,
                    peoplenumber=peoplenumber,
                    reservationstatus="pending",
                    notes=notes or ""
                )
            except Exception as e:
                print(f"Errore nella creazione della roomreservation {e}")

            # update status
            room.status = "taken"
            room.save()

            messages.success(request, f"Prenotazione stanza {room.roomnumber} effettuata!")
            return redirect('HomeLogic')

    context = {
        'ObjHotel': ObjHotel,
        'ObjRoom': ObjRoom,
    }
    return render(request, 'prenotazioni_hotel.html', context)
# events redirect
def events_view(request: HttpRequest):
    try:
        if request.method == "POST":
            choice = request.POST.get('redirect')
            #
            if choice == 'prenotazione_eventi':
                return render(request, 'prenotazioni_eventi.html')
            #
    except Exception as e:
        messages.error(request, f"Error [{e}]")
    #
    return render(request, 'eventi.html')
# events reservarvation view
def events_reservation(request: HttpRequest):

    if request.method == "POST":

        reservation = request.POST.get('redirect')

        if reservation == "reservation":

            # get the user choices
            EventType = request.POST.get('eventtype')
            EventDate = request.POST.get('eventdate')
            EventLocation = request.POST.get('eventlocation')
            GuestsNumber = request.POST.get('guestsnumber')
            Notes = request.POST.get('notes')

            # catch user id if logged in
            user_id = request.session.get('user_id')
            if not user_id:
                messages.warning("Errore. Devi aver fatto il login per richedere location per eventi")
                return redirect('login')

            # check user exist
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                messages.error(request, "Errore: utente non trovato.")
                return redirect('login')

            # get user info
            ObjUser = User.objects.get(id=user_id)

            # check if user choices are correct
            if not all([EventType, EventDate, EventLocation, GuestsNumber]):
                messages.warning("Errore. Devi completare tutti i campi")
                return redirect('events_reservation')

            # check if EventDate is before now
            try:
                Date = datetime.strptime(EventDate, "%Y-%m-%d").date()
                CurrentDate = datetime.today().strptime('%Y-%m-%d')
            except ValueError:
                messages.error(request, "Formato data non valido.")
                return redirect('hotel_reservation')

            if Date <= CurrentDate:
                messages.error(request, "Errore: la data scelta deve essere futura a quella odierna.")
                return redirect('events_reservation')
            
            # create the event
            try:
                Events.objects.create(
                    iduser = user,
                    type = EventType,
                    eventdate = EventDate,
                    location = EventLocation,
                    guestsnumber = GuestsNumber,
                    notes = Notes or ""
                )
            except Exception as e:
                print(f'Errore nella creazione del events_reservation{e}')

    return render(request, 'prenotazioni_eventi.html')
# resturant table redirect
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
    return render(request, 'ristorante.html')
# restaurant table reservation
def restaurant_reservation(request: HttpRequest):

    # Recupera l'oggetto ristorante (in questo esempio è fisso con id=1)
    ObjRestaurant = get_object_or_404(Restaurant, id=1)

    # Recupera tutti i tavoli di quel ristorante ordinati per numero
    ObjTable = Restauranttable.objects.filter(idrestaurant=ObjRestaurant).order_by('tablenumber')

    if request.method == "POST":
        # Campo hidden per capire se l'utente sta prenotando
        reservation = request.POST.get('redirect')

        # Recupera i dati inseriti dall'utente nel form
        table_id = request.POST.get('restauranttable')
        ReservationDate = request.POST.get('reservationdate')   # formato atteso: YYYY-MM-DD
        ReservationTime = request.POST.get('reservationtime')   # formato atteso: HH:MM:SS
        PeopleNumber = request.POST.get('peoplenumber')
        Position = request.POST.get('position')  # inside / outside
        Notes = request.POST.get('notes')

        if reservation == "reservation":
            # --- CONTROLLO LOGIN ---
            user_id = request.session.get('user_id')
            if not user_id:
                messages.warning(request, "Devi effettuare il login per prenotare.")
                return redirect('login')

            # Verifica che l'utente esista nel DB
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                messages.error(request, "Errore: utente non trovato.")
                return redirect('login')

            # --- CONTROLLO CAMPI OBBLIGATORI ---
            if not all([ReservationDate, ReservationTime, PeopleNumber, Position]):
                messages.error(request, "Tutti i campi devono essere compilati.")
                return redirect('restaurant_reservation')

            # --- CONVERSIONE DATA/ORA ---
            try:
                # Trasforma la stringa in oggetto date
                ResDate = datetime.strptime(ReservationDate, "%Y-%m-%d").date()

                # Trasforma la stringa in oggetto time
                ResTime = datetime.strptime(ReservationTime, "%H:%M:%S").time()
            except ValueError:
                # Errore nel formato della data/ora
                messages.error(request, "Formato data/ora non valido.")
                return redirect('restaurant_reservation')

            # --- CONTROLLO DATA FUTURA O OGGI ---
            if ResDate < date.today():
                messages.error(request, "La data scelta deve essere oggi o futura.")
                return redirect('restaurant_reservation')

            # --- CONTROLLO GIORNO DI APERTURA ---
            # Ricava il giorno della settimana della data scelta (in inglese)
            day_name = ResDate.strftime("%A").lower()  # es: "monday"

            # Trasforma la stringa OpeningDays del DB in lista
            opening_days = [d.strip().lower() for d in ObjRestaurant.openingdays.split(",")]
            if day_name not in opening_days:
                messages.error(request, f"Il ristorante è chiuso di {day_name}.")
                return redirect('restaurant_reservation')

            # --- CONTROLLO ORARIO ---
            if not (ObjRestaurant.openingtime <= ResTime <= ObjRestaurant.closingtime):
                messages.error(request, "Orario scelto fuori dall'orario di apertura.")
                return redirect('restaurant_reservation')

            # --- CONTROLLO DISPONIBILITÀ TAVOLO CON POSIZIONE ---
            try:
                table = Restauranttable.objects.get(
                    id=table_id,
                    idrestaurant=ObjRestaurant,
                    position=Position,  # inside / outside
                    status='free'       # deve essere libero
                )
            except Restauranttable.DoesNotExist:
                messages.error(request, "Tavolo non disponibile per la posizione scelta.")
                return redirect('restaurant_reservation')

            # --- CREAZIONE PRENOTAZIONE ---
            Tablereservation.objects.create(
                iduser=user,
                idrestauranttable=table,
                reservationdate=ResDate,
                reservationtime=ResTime,
                peoplenumber=PeopleNumber,
                reservationstatus='pending',  # stato iniziale in attesa
                notes=Notes or ''              # se Notes è None → stringa vuota
            )

            table.status = 'taken'
            table.save()

            # Messaggio di conferma
            messages.success(request, "Prenotazione effettuata con successo!")
            return redirect('restaurant_reservation')

    # Se GET o se non ci sono errori → carica la pagina
    return render(request, 'prenotazioni_ristorante.html', {'ObjTable': ObjTable})
# menu restaurant redirect
def events_menu(request: HttpRequest):
    try:
        if request.method == "POST":
            choice = request.POST.get('redirect')
            if choice == 'menu_eventi':
                return render(request, 'menu_eventi.html')
    except Exception as e:
        print(f"Errore nella visione del menu eventi: [{e}]")
    return render(request, 'eventi.html')
# recipe tortelloni redirect
def tortelloni_views(request: HttpRequest):
    try:
        if request.method == "POST":
            choice = request.POST.get('redirect')
            if choice == 'ricetta_tortelloni':
                return render(request, 'ricetta_tortelloni.html')
    except Exception as e:
        print(f"Errore nella visione della ricetta tortelloni")
    return redirect('restaurant_view')
# recipe tacon redirect
def tacon_views(request: HttpRequest):
    try:
        if request.method == "POST":
            choice = request.POST.get('redirect')
            if choice == 'ricetta_tacon':
                return render(request, 'ricetta_tacon.html')
    except Exception as e:
        print(f"Errore nella visione della ricetta tacon")
    return redirect('restaurant_view')
#
#
#