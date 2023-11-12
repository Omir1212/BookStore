from django.urls import path

from . import views




urlpatterns = [
    path('create-book/', views.CreateBook.as_view(), name='book-creation'),
    path('retrieve-book/<int:pk>/', views.RetrieveBook.as_view(), name='book-retrieval'),
    path('list-books/', views.ListBook.as_view(), name='book-listing'),
    path('update-book/<int:pk>/', views.UpdateBook.as_view(), name='book-update'),
    path('delete-book/<int:pk>/', views.DeleteBook.as_view(), name='book-deletion'),

]
