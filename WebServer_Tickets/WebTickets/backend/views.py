# django import
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.tokens import default_token_generator
from django.http import Http404, HttpRequest
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import ListView
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse

# extra import
import os

from backend.models import (
    Bigliettoabbonamento,
    Metodopagamento,
    Stazione,
    Tratta,
    Treno,
    Trenostazione,
    Utente
)

# Class Based View
# InOut Logic
class InOutLogic(View):
    template_name = 'LogIn.html'
    login_url = 'login_view'

    def get(self, request: HttpRequest):
        return render(request)
    #
    def post(self, request: HttpRequest):
        action = request.POST.get("action")

#
#