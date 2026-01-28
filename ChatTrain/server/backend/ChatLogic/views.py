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

class HTML_FILES(Enum):
    HOME_TEMPLATE = 'home.html',
    ADMIN_PANEL = 'admin_panel.hmtl',
    CUSTOMER_HOME = 'customer_home_page.html',
    CUSTOMER_MACHINE = 'customer_machine_info.html',
    SERVICE_HOME = 'service_home_page.html',
    SERVICE_MACHINE = 'service_machine_info.html',

template = HTML_FILES

# Create your views here.
class HomeLogic(View):

    def get(self, request: HttpRequest):
        return render(request, template.HOME_TEMPLATE.value)
    
    def post(self, request: HttpRequest):
        try:
            action = request.POST.get('action')
            if action == 'login':
                return redirect('login')
            elif action == 'signup':
                return redirect('signup')
        except Exception as e:
            print(f"Exception: [{e}]")
        return render(request, template.HOME_TEMPLATE.value)
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
                return render(request, template.HOME_TEMPLATE.value)
        except Exception as e:
            print(f"Exception Login: [{e}]")
        except Customers.DoesNotExist:
            messages.error(request, "Customer does not exists.")
        except Service.DoesNotExist:
            messages.error(request, "Service does not exists")
    return render(request, template.HOME_TEMPLATE.value)
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
    return render(request, template.HOME_TEMPLATE.value)
#
@service_is_logged_in
def admin_panel(request: HttpRequest):
    return render(request, template.ADMIN_PANEL.value)
#
@service_is_logged_in
def service_home(request: HttpRequest):
    return render(request, template.SERVICE_HOME.value)
#
@service_is_logged_in
def service_machine(request: HttpRequest):
    return render(request, template.SERVICE_MACHINE.value)
#
@customer_is_logged_in
def customer_home(request: HttpRequest):
    return render(request, template.CUSTOMER_HOME.value)
#
@customer_is_logged_in
def customer_machine(request: HttpRequest):
    return render(request, template.CUSTOMER_MACHINE.value)
#
def send_msg(request: HttpRequest):
    try:
        user_id = request.session.get('user_id')
        if not user_id:
            messages.warning(request, "You need to login")
            return redirect('login')
        if request.session.accessed:
            user_info = request.session.save(True)
            print(f"User Info Send msg: [{user_info}]")
    except Exception as e:
        print(e)
        return redirect('HomeLogic')
    return redirect('HomeLogic')
#
def create_ticket(request: HttpRequest, ticket_id):
    pass