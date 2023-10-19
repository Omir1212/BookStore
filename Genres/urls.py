from django.urls import path

from . import views


urlpatterns = [
    
    path('create-genre/', views.CreateGenre.as_view(), name='genre-creation'),
    path('retrieve-genre/<int:pk>/', views.RetrieveGenre.as_view(), name='genre-retrieval'),
    path('list-genres/', views.ListGenre.as_view(), name='genre-listing'),
    path('update-genre/<int:pk>/', views.UpdateGenre.as_view(), name='genre-update'),
    path('delete-genre/<int:pk>/', views.DeleteGenre.as_view(), name='genre-deletion'),

]
