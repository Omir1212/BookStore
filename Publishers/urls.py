from django.urls import path

from . import views





urlpatterns = [
    
    path('create-publisher/', views.CreatePublisher.as_view(), name='publisher-creation'),
    path('retrieve-publisher/<int:pk>/', views.RetrievePublisher.as_view(), name='publisher-retrieval'),
    path('list-publishers/', views.ListPublisher.as_view(), name='publisher-listing'),
    path('update-publisher/<int:pk>/', views.UpdatePublisher.as_view(), name='publisher-update'),
    path('delete-publisher/<int:pk>/', views.DeletePublisher.as_view(), name='publisher-deletion'),

]
