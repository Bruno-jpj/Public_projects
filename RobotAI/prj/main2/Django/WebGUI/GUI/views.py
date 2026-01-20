from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.http import Http404, HttpRequest, HttpResponse # HttpResponse -> generic & need manual content for JSON
from django.views import View
from django.http import JsonResponse # -> JSON specific & automatic
from django.utils import timezone

from GUI.extra.conn_db import conn_db

from GUI.models import Cmd

#from rest_framework import generics

# set command
SET_CMD = {
    00: "None",
    11: "Stop",
    22: "Start",
    33: "Move to [{x},{y}] position"
}

# var to store last command
LastCommand = {"command": "None"}

# Create your views here.
class Index(View):
    BASE_TEMPLATE = 'index.html'

    # -> called when used in urls.py for routing
    def get(self, request: HttpRequest):
        return render(request, self.BASE_TEMPLATE)
    # post -> when called in a html file
    def post(self, request: HttpRequest):
        pass
# Start Auto Exp
def start(request: HttpRequest):
    try:
        current_time = timezone.now()
        if request.method == "POST":
            choice = request.POST.get('submit')
            if choice == 'start':
                if conn_db(current_time, SET_CMD[22], None, None):
                    messages.success(request, "Comand inserted successfuly. ")
                    response = {"status":"ok"}
                else:
                    messages.error(request, "Comand not inserted, view the log.")
                    response = {"status":"error"}
        #
        LastCommand.update({"command":SET_CMD.get(22)})
        request.session['response'] = response
        #
        return redirect("send")
    except Exception as e:
        print(f"Exception catched: [{e}]")
        return JsonResponse({"status":"error start"})
# Stop 
def stop(request: HttpRequest):
    try:
        current_time = timezone.now()
        if request.method == "POST":
            choice = request.POST.get('submit')
            if choice == 'stop':
                if conn_db(current_time, SET_CMD[11], None, None):
                    messages.success(request, "Comand inserted successfuly. ")
                    response = {"status":"ok"}
                else:
                    messages.error(request, "Comand not inserted, view the log.")
                    response = {"status":"error"}
        #
        LastCommand.update({"command":SET_CMD.get(11)})
        request.session['response'] = response
        #
        return redirect("send")
    except Exception as e:
        print(f"Exception catched: [{e}]")
        return JsonResponse({"status":"error stop"})
# Move to (X,Y)
def move(request: HttpRequest):
    try:
        current_time = timezone.now()
        if request.method == "POST":
            choice = request.POST.get('submit')
            if choice == 'move':
                valx = request.POST.get('Xinput')
                valy = request.POST.get('Yinput')
                #
                x = int(valx)
                y = int(valy)
                #
                if not all([x, y]):
                    messages.error(request, "Don't leave any fields empty")
                if not (valx.isnumeric() and valy.isnumeric()):
                    messages.error(request, "All fields must be numeric")
                #
                if conn_db(current_time, SET_CMD[33], x, y):
                    messages.success(request, "Comand inserted successfuly. ")
                    response = {"status":"ok"}
                else:
                    messages.error(request, "Comand not inserted, view the log.")
                    response = {"status":"error"}
        #
        LastCommand.update({"command":SET_CMD.get(33),"x":x,"y":y}) 
        request.session['response'] = response
        #
        return redirect('send')
    except Exception as e:
        print(f"Exception catched: [{e}]")
        return JsonResponse({"status":"error move"})
# send command view
def send_command(request: HttpRequest):

    try:
        cmd_status = request.session.get('response')
        print(f"Command Status: [{cmd_status}]")

        print(f"Sending last command: {LastCommand}")
    except Exception as e:
        print(f"Exception catched in send_command: [{e}]")
    return JsonResponse(LastCommand)
#