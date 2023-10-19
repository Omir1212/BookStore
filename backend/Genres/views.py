from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from .models import  Genre 
from .serializers import  GenreSerializer 



class CreateGenre(GenericAPIView, CreateModelMixin ):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class RetrieveGenre(GenericAPIView, RetrieveModelMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

class ListGenre(GenericAPIView, ListModelMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class UpdateGenre(GenericAPIView, UpdateModelMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class DeleteGenre(GenericAPIView, DestroyModelMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
