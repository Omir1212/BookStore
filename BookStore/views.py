from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from .models import Book , Author , Genre , Publisher , Customer , Order , Review
from .serializers import BookSerializer , AuthorSerializer , GenreSerializer , PublisherSerializer , CustomerSerializer , OrderSerializer , ReviewSerializer




class CreateBook(GenericAPIView, CreateModelMixin ):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class RetrieveBook(GenericAPIView, RetrieveModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    


class ListBook(GenericAPIView, ListModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class UpdateBook(GenericAPIView, UpdateModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 
    

class DeleteBook(GenericAPIView, DestroyModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

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
    

