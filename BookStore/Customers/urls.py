from django.urls import path

from . import views


urlpatterns = [
    
    path('create-customer/', views.CreateCustomer.as_view(), name='user-creation'),
    path('retrieve-customer/<int:pk>/', views.RetrieveCustomer.as_view(), name='user-retrieval'),
    path('list-customers/', views.ListCustomer.as_view(), name='user-listing'),
    path('update-customer/<int:pk>/', views.UpdateCustomer.as_view(), name='user-update'),
    path('delete-customer/<int:pk>/', views.DeleteCustomer.as_view(), name='user-deletion'),

]