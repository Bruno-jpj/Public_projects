from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpRequest, HttpResponse, Http404
from django.views import View

# Create your views here.
class HomeLogic(View):
    TEMPLATE = 'home.html'

    def get(self, request: HttpRequest):
        return render(request, self.TEMPLATE)
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