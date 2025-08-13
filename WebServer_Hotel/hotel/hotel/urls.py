"""
URL configuration for hotel project.

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
    HomeLogic,
    login,
    logout,
    signup,
    events_reservation,
    events_view,
    hotel_reservation,
    hotel_view,
    resturant_reservation,
    resturant_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeLogic.as_view(), name="home"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', logout, name="logout"),
    path('events_reservation/', events_reservation, name="events_res"),
    path('events_view/', events_view, name="events"),
    path('hotel_reservation/', hotel_reservation, name="hotel_res"),
    path('hotel_view/', hotel_view, name="hotel"),
    path('restaurant_reservation/', resturant_reservation, name="restaurant_res"),
    path('restaurant_view/', resturant_view, name="restaurant")
]
