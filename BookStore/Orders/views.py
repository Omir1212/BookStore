from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from .models import Book , Author , Genre , Publisher , Customer , Order , Review
from .serializers import BookSerializer , AuthorSerializer , GenreSerializer , PublisherSerializer , CustomerSerializer , OrderSerializer , ReviewSerializer


class CreateOrder(GenericAPIView, CreateModelMixin ):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class RetrieveOrder(GenericAPIView, RetrieveModelMixin):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ListOrder(GenericAPIView, ListModelMixin):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class UpdateOrder(GenericAPIView, UpdateModelMixin):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class DeleteOrder(GenericAPIView, DestroyModelMixin):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
