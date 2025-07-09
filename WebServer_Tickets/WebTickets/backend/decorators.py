from django.http import HttpRequest, Http404, HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from backend.models import Utente

def user_is_logged_in(func):
    """
    Decoratore per le viste che richiede all'utente di essere loggato.
    Se l'utente non è loggato, reindirizza alla pagina di login
    e mostra un messaggio.
    """
    def wrapper(request: HttpRequest, *args, **kwargs):
        # prendo id utente dalla sessione
        user_id = request.session.get('user_id')
        
        # se l'id esiste
        if user_id is not None:
            try:
                # creo oggetto utente controllando che esista con l'id preso e quello del DB
                User_obj = Utente.objects.get(id = user_id)

                # stampo id e username
                print(f"ID User: [{user_id}] & UserName: [{User_obj.username}]")

                # senza errori ritorna la func a cui è collegata
                return func(request, *args, **kwargs)
            except Exception as e:
                messages.info(request, f"L'utente non è più valido. Effettua nuovamente il login. Codice Errore: [{e}]")
                return redirect('login')
        else:
            messages.info(request, "Devi effetturare l'accesso per visualizzare questa pagina")
            return redirect('login')
    return wrapper
#