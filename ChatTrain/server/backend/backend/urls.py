"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from ChatLogic.views import (
    HomeLogic,
    login,
    signup,
    service_home,
    service_machine,
    customer_home,
    customer_machine,
    send_msg,
    create_ticket,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeLogic.as_view(), name='home'),
    path('customer_home/', customer_home, name='customer_home'),
    path('service_home/', service_home, name='service_home'),
    path('customer_machine/', customer_machine, name='customer_info'),
    path('service_machine', service_machine, name='service_info'),
    path('sent_msg/', send_msg, name='send_msg'),
    path('create_ticket/', create_ticket, name='create_ticket')
]
