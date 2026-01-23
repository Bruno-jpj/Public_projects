from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.views import View

# Create your views here.

class HomeLogic(View):
    HOME_TEMPLATE = 'home.html'

    def get(self, request: HttpRequest):
        return render(request, self.HOME_TEMPLATE)
    
    def post(self, request: HttpRequest):
        return render(request, self.HOME_TEMPLATE)