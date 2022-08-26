from django.urls import path, include
from app_users.views import login_view, AnotherLoginView, logout_view, AnotherLogoutView

urlpatterns = [
    #path('', login_view, name='login'),
    path('login', AnotherLoginView.as_view(), name='another_login'),
    #path('logout', logout_view, name='another_logout'),
    path('logout', AnotherLogoutView.as_view(), name='another_logout'),
    path('home/', include('reg.urls'), name='home'),
]