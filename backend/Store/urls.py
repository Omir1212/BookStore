from django.conf import settings
from django.contrib import admin
from django.urls import path , re_path, include
from django.conf.urls.static import serve
from dj_rest_auth.views import LoginView, LogoutView, PasswordResetView
from dj_rest_auth.registration.views import VerifyEmailView, RegisterView



urlpatterns = [

    # Admin Routes
    path('admin/', admin.site.urls),

    # Restframework Routes
    path('api-auth/', include('rest_framework.urls')),

    # Modules Routes
    path('api/auth/', include('dj_rest_auth.urls')),
    path('Books/', include('Books.urls')),
    path('Authors/', include('Authors.urls')),
    path('Genres/', include('Genres.urls')),
    path('Publishers/', include('Publishers.urls')),
    path('Customers/', include('Customers.urls')),
    path('Orders/', include('Orders.urls')),
    path('Reviews/', include('Reviews.urls')),

    # Authentication Routes
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('api/auth/account-confirm-email/<str:key>/', VerifyEmailView.as_view(), name='account_confirm_email'),
    path('api/auth/login/', LoginView.as_view(), name='rest_login'),
    path('api/auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/auth/password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('api/auth/registration/', RegisterView.as_view(), name='rest_register'),

    
]