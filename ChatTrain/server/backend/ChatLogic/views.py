from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.views import View

from enum import Enum
from backend.decorators import (
    customer_is_logged_in,
    service_is_logged_in
)
from ChatLogic.models import (
    Service,
    Machine,
    Customers,
    Customermachine,
    Tickets
)

HOME_TEMPLATE = 'home.html'

# Create your views here.
class HomeLogic(View):
    
    def get(self, request: HttpRequest):
        return render(request, HOME_TEMPLATE)
    
    def post(self, request: HttpRequest):
        try:
            action = request.POST.get('action')
            if action == 'login':
                return redirect('login')
            elif action == 'signup':
                return redirect('signup')
        except Exception as e:
            print(f"Exception: [{e}]")
        return render(request, HOME_TEMPLATE)
#
def login(request: HttpRequest, response: HttpResponse):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 
        #
        try:
            # check if user is assistance
            if username.startswith("SAC") and Service.objects.get(is_admin = 0): # Service Assistance Code
                service_user = Service.objects.get(serv_code = username)

                if check_password(password, service_user.serv_pwd):
                    request.session['username_id'] = service_user.id
                    return redirect('service_home')
                
            elif username.startswith("AAC") and Service.objects.get(is_admin = 1): # Admin Assistance Code
                admin_user = Service.objects.get(serv_code = username)

                if check_password(password, admin_user.serv_pwd):
                    request.session['username_id'] = admin_user.id
                    return redirect('service_home')
                
            elif username.startswith("CU"): # Customer Username
                customer_user = Customers.objects.get(username = username)

                if check_password(password, customer_user.pwd):
                    request.session['customer_id'] = customer_user.id
                    return redirect('customer_home')
            else:
                return render(request, HOME_TEMPLATE)
        except Exception as e:
            print(f"Exception Login: [{e}]")
        except Customers.DoesNotExist:
            messages.error(request, "Customer does not exists.")
        except Service.DoesNotExist:
            messages.error(request, "Service does not exists")
    return render(request, HOME_TEMPLATE)
#
def signup(request: HttpRequest, response: HttpResponse):
    if request.method == "POST":
        customer_username = request.POST.get("username")
        customer_password = request.POST.get("password")
        customer_name = request.POST.get("customer")
        #
        if not all([customer_username, customer_password, customer_name]):
            messages.error(request, "Error: Please insert into all fields")
        #
        if len(customer_password) < 8:
            messages.error(request, "Error: Password must be at least 8 characters")
        #
        if Customers.objects.filter(buyer_name = customer_name).exists() or Customers.objects.filter(username = customer_username):
            messages.error(request, "Error: Customer already exists")
        #
        try:
            hashed_password = make_password(customer_password)
            customer = Customers.objects.create(
                buyer_name = customer_name,
                username = customer_username,
                pwd = hashed_password
            )
            messages.success(request, "User created successfuly")
        except Exception as e:
            messages.error(request, f"Error: Customer not created [{e}]")
    return render(request, HOME_TEMPLATE)
#
@service_is_logged_in
def admin_panel(request: HttpRequest):
    pass
#
@service_is_logged_in
def service_home(request: HttpRequest):
    pass
#
@service_is_logged_in
def service_machine(request: HttpRequest):
    pass
#
@customer_is_logged_in
def customer_home(request: HttpRequest):
    pass
#
@customer_is_logged_in
def customer_machine(request: HttpRequest):
    pass
#