from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter
#
# book_router = DefaultRouter()
# book_router.register(r'book', views.BookView, basename='book-view')

urlpatterns = [
    path('create/', views.CreateBook.as_view(), name='create-book'),
    path('list/', views.ListBooks.as_view(), name='list-books'),
    path('book/<int:pk>/', views.RetrieveUpdateBook.as_view(), name='update-book'),
    path('delete/<int:pk>/', views.DeleteBook.as_view(), name='delete-book'),
    # path('', include(book_router.urls))
]


