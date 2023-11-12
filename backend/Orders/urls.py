from django.urls import path

from . import views


urlpatterns = [
    
    path('create-order/', views.CreateOrder.as_view(), name='order-creation'),
    path('retrieve-order/<int:pk>/', views.RetrieveOrder.as_view(), name='order-retrieval'),
    path('list-orders/', views.ListOrder.as_view(), name='order-listing'),
    path('update-order/<int:pk>/', views.UpdateOrder.as_view(), name='order-update'),
    path('delete-order/<int:pk>/', views.DeleteOrder.as_view(), name='order-deletion'),

]
