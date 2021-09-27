from django.urls import path
from user.views import signin
from django.shortcuts import redirect



urlpatterns = [
    path('signin/', signin, name='signin_page'),
    # path('login/', signin, name='login_page'),
    # path('', lambda request: redirect('/user/login/')),
]