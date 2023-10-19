from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from .models import Author 
from .serializers import  AuthorSerializer 



class CreateAuthor(GenericAPIView, CreateModelMixin ):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class RetrieveAuthor(GenericAPIView, RetrieveModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

class ListAuthor(GenericAPIView, ListModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class UpdateAuthor(GenericAPIView, UpdateModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class DeleteAuthor(GenericAPIView, DestroyModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

