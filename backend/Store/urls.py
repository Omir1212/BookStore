from django.conf import settings
from django.contrib import admin
from django.urls import path , re_path, include
from django.conf.urls.static import serve
from dj_rest_auth.views import LoginView, LogoutView, PasswordResetView
from dj_rest_auth.registration.views import VerifyEmailView, RegisterView








urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('Books/', include('Books.urls')),
    path('Authors/', include('Authors.urls')),
    path('Genres/', include('Genres.urls')),
    path('Publishers/', include('Publishers.urls')),
    path('Customers/', include('Customers.urls')),
    path('Orders/', include('Orders.urls')),
    path('Reviews/', include('Reviews.urls')),
    
]