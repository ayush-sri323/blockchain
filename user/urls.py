from django.contrib import admin
from django.urls import path, include
from user.views.login import LoginView
from user.views.logout import Logout
from user.views.signup import Signup

urlpatterns = [
    path('v1/login', LoginView.as_view()),
    path('v1/logout', Logout.as_view(), name='logout'),
    path('v1/signup', Signup.as_view(), name='signup'),
]

