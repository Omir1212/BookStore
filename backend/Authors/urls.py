from django.urls import path

from . import views




urlpatterns = [
    path('create-author/', views.CreateAuthor.as_view(), name='author-creation'),
    path('retrieve-author/<int:pk>/', views.RetrieveAuthor.as_view(), name='author-retrieval'),
    path('list-authors/', views.ListAuthor.as_view(), name='author-listing'),
    path('update-author/<int:pk>/', views.UpdateAuthor.as_view(), name='author-update'),
    path('delete-author/<int:pk>/', views.DeleteAuthor.as_view(), name='author-deletion'),

]
