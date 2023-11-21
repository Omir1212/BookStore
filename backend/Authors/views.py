from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from .models import Author 
from .serializers import AuthorSerializer 
from rest_framework import generics, mixins
from .models import Author
from .serializers import AuthorSerializer



# class CreateAuthor(GenericAPIView, mixins.CreateModelMixin ):
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class RetrieveAuthor(GenericAPIView, mixins.RetrieveModelMixin):
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    

# class ListAuthor(GenericAPIView, mixins.ListModelMixin):
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    

# class UpdateAuthor(GenericAPIView, mixins.UpdateModelMixin):
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    

class AuthorListCreateView(generics.ListCreateAPIView):
            queryset = Author.objects.all()
            serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
            queryset = Author.objects.all()
            serializer_class = AuthorSerializer
