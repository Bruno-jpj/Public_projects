
from django.contrib import admin
from django.urls import path

from backend.views import (
    site_list_view, 
    home_page_view, 
    login_index_view, 
    log_out_view, 
    site_create_view,
    dynamic_site_view,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_index_view, name='login_index_view'),
    path('home/',home_page_view, name='home_page_view'),
    path('site/', site_list_view, name='site_list_view'),
    path('logout/', log_out_view, name='log_out_view'),
    path('create/',site_create_view, name='site_create_view'),

    # dynamic routing: 
    path('site/<slug:slug>', dynamic_site_view, name='dynamic_site_view'), 
]