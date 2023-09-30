from django.urls import path

from . import views


urlpatterns = [
  
    path('create-review/', views.CreateReview.as_view(), name='review-creation'),
    path('retrieve-review/<int:pk>/', views.RetrieveReview.as_view(), name='review-retrieval'),
    path('list-reviews/', views.ListReview.as_view(), name='review-listing'),
    path('update-review/<int:pk>/', views.UpdateReview.as_view(), name='review-update'),
    path('delete-review/<int:pk>/', views.DeleteReview.as_view(), name='review-deletion'),

]
