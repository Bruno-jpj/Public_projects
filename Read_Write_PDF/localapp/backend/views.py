from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views import View
from django.contrib import messages

from backend.decorators import (
    show_pdf,
)

# Create your views here.

class HomePage(View):
    TEMPLATE = 'home.html'

    @show_pdf
    def get(self, request: HttpRequest):
        context = {
            'pdf_files': request.pdf_files
        }
        return render(request, self.TEMPLATE, context)
    #
    @show_pdf
    def post(self, request: HttpRequest):
        if request.method == "POST":
            #
            btn_action = request.POST.get('action')
            #
            if btn_action == 'read':
                print("read PDF")
            elif btn_action == 'write':
                print("write PDF")
            elif btn_action == 'save':
                print("save PDF")
            else:
                print("Form Error. Coouldn't catch btn values")
                messages.error(request, "Form Error. Coouldn't catch btn values")
        #
        context = {
            'pdf_files': request.pdf_files
        }
        #
        return render(request, self.TEMPLATE, context)
    #
#
def help(request: HttpRequest):
    return render(request, 'help.html')
#
