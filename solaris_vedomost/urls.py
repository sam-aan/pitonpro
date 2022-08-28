from django.urls import path, include
from solaris_vedomost.views import

urlpatterns = [
    #path('', login_view, name='login'),
    path('', AnotherLoginView.as_view(), name='another_login'),
    #path('logout', logout_view, name='another_logout'),
    path('logout', AnotherLogoutView.as_view(), name='another_logout'),
    path('home/', include('reg.urls'), name='home'),
]