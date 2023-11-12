from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from .models import  Customer
from .serializers import  CustomerSerializer


class CreateCustomer(GenericAPIView, CreateModelMixin ):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class RetrieveCustomer(GenericAPIView, RetrieveModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

class ListCustomer(GenericAPIView, ListModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UpdateCustomer(GenericAPIView, UpdateModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    


class DeleteCustomer(GenericAPIView, DestroyModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

