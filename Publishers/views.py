from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from .models import  Publisher 
from .serializers import PublisherSerializer 




class CreatePublisher(GenericAPIView, CreateModelMixin ):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class RetrievePublisher(GenericAPIView, RetrieveModelMixin):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

class ListPublisher(GenericAPIView, ListModelMixin):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class UpdatePublisher(GenericAPIView, UpdateModelMixin):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeletePublisher(GenericAPIView, DestroyModelMixin):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    