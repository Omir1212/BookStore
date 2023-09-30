from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from .models import Book , Author , Genre , Publisher , Customer , Order , Review
from .serializers import BookSerializer , AuthorSerializer , GenreSerializer , PublisherSerializer , CustomerSerializer , OrderSerializer , ReviewSerializer





class CreateReview(GenericAPIView, CreateModelMixin ):

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class RetrieveReview(GenericAPIView, RetrieveModelMixin):

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    


class ListReview(GenericAPIView, ListModelMixin):
    
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

class UpdateReview(GenericAPIView, UpdateModelMixin):
    
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        

class DeleteReview(GenericAPIView, DestroyModelMixin):

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

