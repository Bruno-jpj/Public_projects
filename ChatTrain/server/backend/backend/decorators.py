from django.http import HttpRequest, Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from ChatLogic.models import (
    Customers,
    Service,
)

def customer_is_logged_in(func):
    def wrapper(request: HttpRequest, *args, **kwargs):
        # take customerID from session
        customer_id = request.session.get('customer_id')

        if customer_id is not None:
            try:
                # create customer obj checking it exists in the DB
                service_obj = Customers.objects.get(id = customer_id)
                # print the customer info
                print(f"Customer Username: {service_obj.username} | Customer Name{service_obj.buyer_name}")

                return func(request, *args, **kwargs)
            except Exception as e:
                messages.info(request, f"Username not valid. Please retry. Error Code [{e}]")
                return redirect("HomeLogic")
        else:
            messages.info(request, "Please try to login first")
            print("decorator here.....")
            return HttpResponse("Hi from decorator. Customer didn't logged in.")
    return wrapper
#
def service_is_logged_in(func):
    def wrapper(request: HttpRequest, *args, **kwrags):
        # take serviceID from session
        service_id = request.session.get('service_id')

        if service_id is not None:
            try:
                # create customer obj checking it exists in the DB
                service_obj = Service.objects.get(id = service_id)
                # print the customer info
                print(f"Customer Username: {service_obj.serv_code}")

                return func(request, *args, **kwrags)
            except Exception as e:
                messages.info(request, f"Username not valid. Please retry. Error Code [{e}]")
                return redirect('HomeLogic')
        else:
            messages.info(request, "Please try to login first")
            #return redirect("Service not logged in..... HI from decorator")
            return HttpResponse("Hi from decorator. Service/Admin didn't logged in.")
    return wrapper