from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import BookSerializer
from .models import Book



# Create your views here.

class CreateBook(CreateAPIView):
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListBooks(ListAPIView):
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
    queryset = Book.objects.all()

    def get_queryset(self):
        queryset = Book.objects.filter(Q(price=200) & Q(author_name='Omir Hosny'))
        return queryset


class RetrieveUpdateBook(RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class DeleteBook(DestroyAPIView):
    queryset = Book.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
