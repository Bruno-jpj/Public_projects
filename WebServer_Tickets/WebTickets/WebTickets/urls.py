"""
URL configuration for WebTickets project.

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
from backend.views import (
    login_view,
    log_out_view,
    signup_view,
    home_view,
    find_station_view,
    account_view,
    info_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('account/', account_view, name='account_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', log_out_view, name='log_out_view'),
    path('signup/', signup_view, name='signup_view'),
    path('findstation/', find_station_view, name='find_station_view'),
    path('info/', info_view, name='info_view')
]
