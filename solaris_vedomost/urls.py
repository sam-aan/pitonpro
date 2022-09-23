from django.urls import path, include
from . import views
from app_users.views import AnotherLogoutView

urlpatterns = {
    path('logout', AnotherLogoutView.as_view(), name='another_logout'),
    path('home', include('reg.urls'), name='home'),
    path('sol', views.sol_ved, name='solved'),
}
