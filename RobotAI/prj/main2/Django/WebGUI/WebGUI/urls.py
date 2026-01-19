"""
URL configuration for WebGUI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from GUI.views import (
    start,
    stop,
    move,
    Index,
    send_command
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(),name="index"),
    path('start/', start, name="start"),
    path('stop/', stop, name="stop"), 
    path('move/', move, name="move"),
    path('send_command/', send_command, name="send")
]