from django.urls import path

from . import views


urlpatterns = [
    path('create-book/', views.CreateBook.as_view(), name='book-creation'),
    path('retrieve-book/<int:pk>/', views.RetrieveBook.as_view(), name='book-retrieval'),
    path('list-books/', views.ListBook.as_view(), name='book-listing'),
    path('update-book/<int:pk>/', views.UpdateBook.as_view(), name='book-update'),
    path('delete-book/<int:pk>/', views.DeleteBook.as_view(), name='book-deletion'),

    path('create-author/', views.CreateAuthor.as_view(), name='author-creation'),
    path('retrieve-author/<int:pk>/', views.RetrieveAuthor.as_view(), name='author-retrieval'),
    path('list-authors/', views.ListAuthor.as_view(), name='author-listing'),
    path('update-author/<int:pk>/', views.UpdateAuthor.as_view(), name='author-update'),
    path('delete-author/<int:pk>/', views.DeleteAuthor.as_view(), name='author-deletion'),

    path('create-genre/', views.CreateGenre.as_view(), name='genre-creation'),
    path('retrieve-genre/<int:pk>/', views.RetrieveGenre.as_view(), name='genre-retrieval'),
    path('list-genres/', views.ListGenre.as_view(), name='genre-listing'),
    path('update-genre/<int:pk>/', views.UpdateGenre.as_view(), name='genre-update'),
    path('delete-genre/<int:pk>/', views.DeleteGenre.as_view(), name='genre-deletion'),

    path('create-publisher/', views.CreatePublisher.as_view(), name='publisher-creation'),
    path('retrieve-publisher/<int:pk>/', views.RetrievePublisher.as_view(), name='publisher-retrieval'),
    path('list-publishers/', views.ListPublisher.as_view(), name='publisher-listing'),
    path('update-publisher/<int:pk>/', views.UpdatePublisher.as_view(), name='publisher-update'),
    path('delete-publisher/<int:pk>/', views.DeletePublisher.as_view(), name='publisher-deletion'),

    path('create-user/', views.CreateCustomer.as_view(), name='user-creation'),
    path('retrieve-user/<int:pk>/', views.RetrieveCustomer.as_view(), name='user-retrieval'),
    path('list-users/', views.ListCustomer.as_view(), name='user-listing'),
    path('update-user/<int:pk>/', views.UpdateCustomer.as_view(), name='user-update'),
    path('delete-user/<int:pk>/', views.DeleteCustomer.as_view(), name='user-deletion'),

    path('create-order/', views.CreateOrder.as_view(), name='order-creation'),
    path('retrieve-order/<int:pk>/', views.RetrieveOrder.as_view(), name='order-retrieval'),
    path('list-orders/', views.ListOrder.as_view(), name='order-listing'),
    path('update-order/<int:pk>/', views.UpdateOrder.as_view(), name='order-update'),
    path('delete-order/<int:pk>/', views.DeleteOrder.as_view(), name='order-deletion'),

    path('create-orderitem/', views.CreateOrder.as_view(), name='orderitem-creation'),
    path('retrieve-orderitem/<int:pk>/', views.RetrieveOrder.as_view(), name='orderitem-retrieval'),
    path('list-orderitems/', views.ListOrder.as_view(), name='orderitem-listing'),
    path('update-orderitem/<int:pk>/', views.UpdateOrder.as_view(), name='orderitem-update'),
    path('delete-orderitem/<int:pk>/', views.DeleteOrder.as_view(), name='orderitem-deletion'),

    path('create-review/', views.CreateReview.as_view(), name='review-creation'),
    path('retrieve-review/<int:pk>/', views.RetrieveReview.as_view(), name='review-retrieval'),
    path('list-reviews/', views.ListReview.as_view(), name='review-listing'),
    path('update-review/<int:pk>/', views.UpdateReview.as_view(), name='review-update'),
    path('delete-review/<int:pk>/', views.DeleteReview.as_view(), name='review-deletion'),

    
  

]







