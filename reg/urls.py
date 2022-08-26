# reg/urls.py
from django.urls import path, include
from . import views
from app_users.views import login_view, AnotherLoginView, AnotherLogoutView

urlpatterns = [
    path('glavn', views.glavn, name='home'),
    path('regis', views.regis, name='regis'),
    path('inreg', views.inreg, name='inreg'),
    path('logout', AnotherLogoutView.as_view(), name='logout'),
]