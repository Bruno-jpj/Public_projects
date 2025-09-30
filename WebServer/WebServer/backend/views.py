from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import ( Site, User )
from .forms import SiteCreateForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.http import Http404, HttpRequest
from backend.signals import send_telegram_message as stm
from django.views.generic import ListView #

# Create your views here.

# view per aggiunta del sito 
def site_create_view(request: HttpRequest):
    if 'user_id' not in request.session:
        return redirect('login_index_view')
    #
    # Ottieni i dettagli dell'utente nella sessione
    user_id = request.session['user_id']

    # verifica se l'utente esiste nel db in caso ritorna alla login
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login_index_view')
    
    print(f"User nella home page: [{user}]")
    #
    if request.method == "POST":
        form = SiteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            form = SiteCreateForm() # resetta il form con uno pulito
            return render(request, "site_create.html", {'form':form, 'success':True})
    else:
        form = SiteCreateForm()
    return render(request, "site_create.html",{'form':form})
#
# view per la login 
def login_index_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verifica se l'utente esiste nel database personalizzato
        try:
            #
            user = User.objects.get(Username=username)
            
            # Verifica la pwd con la funzione check_password -> funziona solo se la pwd è criptata altrimenti No
            if check_password(password, user.Password):

                # serve per memorizzare l'ID dell'utente autenticato durante la sessione aperta
                # la sessione viene salvata lato server, è utile per sapere quale utente è loggato
                request.session['user_id'] = user.id    

                stm(user.Username)

                # se il login è corretto reinderizza alla home_page
                return redirect("home_page_view")
            else: 
                messages.error(request, "Username o Password errati!")
        except User.DoesNotExist:
            messages.error(request, "Username o Password non esistenti!")

    # ricarica la pagina di login se fallisce
    return render(request, "login.html")
#
# sistema di logout per eliminare la sessione quando l'utente esce.
def log_out_view(request: HttpRequest):
    try:
        # prova a rimuovere dalla sessione l'oggetto user_id
        del request.session['user_id']

    # quando provi ad accedere a una chiave che non esiste in un dizionario o simile, come request.session
    except KeyError:
        pass
    return redirect("login_index_view")
#
# view per controllare chi è nella home
def home_page_view(request):
    # se user_id non è nella sessione
    if 'user_id' not in request.session:

        # Reindirizza al login se l'utente non è autenticato
        return redirect('login_index_view')  

    # Ottieni i dettagli dell'utente nella sessione
    user_id = request.session['user_id']

    # verifica se l'utente esiste nel db in caso ritorna alla login
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login_index_view')
    
    print(f"User nella home page: [{user}]")

    return render(request, 'home_page.html', {'user': user})
#
# view per gestione della pagina siti 
def site_list_view(request: HttpRequest):
    if 'user_id' not in request.session:
        return redirect('login_index_view')
    
    # Ottieni i dettagli dell'utente nella sessione
    user_id = request.session['user_id']

    # verifica se l'utente esiste nel db in caso ritorna alla login
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login_index_view')
    
    print(f"User nella home page: [{user}]")

    # prende richiesta tipo get dall'html quando viene premuto btn per filtrare
    #                                  ('nome btn',value passata) ==> valori del btn nell'html --> name="paid" value="true"
    paid_site_filter = request.GET.get('paid',None)
    category_site_filter = request.GET.get('category',None)

    # converto la str to lower ->  per gestire varianti come 'TRUE', 'false', ecc.
    if paid_site_filter is not None:
        paid_site_filter = paid_site_filter.lower()

    # prende tutti i siti dal DB - inizializza il queryset, anche se nessun filtro è attivo.
    sites = Site.objects.all()

    # controlli
    if paid_site_filter == 'true':
        # prende i siti paid = true
        sites = Site.objects.filter(paid=True)
    elif paid_site_filter == 'false':
        sites = Site.objects.filter(paid=False)
    #
    if category_site_filter:
        sites = sites.filter(category=category_site_filter)
    #
    context = {
        'sites': sites, # lista di oggetti (in questo caso i siti nel DB)
        'category_choices': Site.CATEGORY_CHOICES,
    }
    return render(request,'site_page.html', context)
#
# dynamic routing per i dettagli specifici del sito
def dynamic_site_view(request: HttpRequest, slug):
    if 'user_id' not in request.session:
        return redirect('login_index_view')
    #
    # Ottieni i dettagli dell'utente nella sessione
    user_id = request.session['user_id']

    # verifica se l'utente esiste nel db in caso ritorna alla login
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login_index_view')
    
    print(f"User nella home page: [{user}]")
 
    try:
        site = Site.objects.get(slug=slug)
    except Site.DoesNotExist:
        raise Http404
    context = {
        'site': site,
    }

    return render(request,'site_detail.html', context)
    # return render(request,'site_detail.html',{'site':site})
#