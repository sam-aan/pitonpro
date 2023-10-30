# reg/urls.py
from django.urls import path, include

from . import views
from app_users.views import AnotherLogoutView
from solaris_vedomost.views import sol_ved, spis_zakaz

urlpatterns = [
    path('glavn', views.glavn, name='home'),
    path('regis', views.regis, name='regis'),
    path('inreg', views.inreg, name='inreg'),
    path('logout', AnotherLogoutView.as_view(), name='logout'),
    path('sol/', sol_ved, name='solved'),
    path('zakaz/', spis_zakaz, name='zakazi'),
]
