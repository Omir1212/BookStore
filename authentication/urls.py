# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/user/', views.register_user, name='register_user'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/author/', views.register_author, name='register_author'),
    path('login/', views.login, name='login'),
]
